import Foundation
import AppKit
import Cocoa

// initialize the application
NSApplication.shared()

// hide the dock icon (same as LSUIElement true in Info.plist)
NSApp.setActivationPolicy(.accessory)

var app = NSApplication.shared()
var menuBar = NSMenu()

var appMenu = NSMenu()

let statusItem = NSStatusBar.system().statusItem(withLength: NSVariableStatusItemLength)
statusItem.menu = appMenu

var enabled = true

let settings = Settings()
var users = [[]]

func updateMenuTitle()
{
    let status = getOwnChargeInfo()
    statusItem.title = "\(status.percent)% \(status.icon)"
}
func updateMenuBar(users: Array<Array<Any>>)
{
    appMenu.removeAllItems()
    
    // create some status bar entries
    let appMenuItem = NSMenuItem()
    menuBar.addItem(appMenuItem)
    app.mainMenu = menuBar
    
    for user in users
    {
        let info = ChargeInfo(user: user)
        
        let view = ElecsRow(info)
        let curUserButton = NSMenuItem(title: view.summary, action: #selector(Settings.toggleReporting), keyEquivalent: "")
        curUserButton.view = view
        curUserButton.target = Settings.self
        appMenu.addItem(curUserButton)
    }

    let reporting = NSMenuItem(title: "Report Charge", action:#selector(Settings.toggleReporting), keyEquivalent: "")
    reporting.target = Settings.self
    reporting.state = enabled ? NSOnState : NSOffState
    appMenu.addItem(reporting)
    
    let prefs = NSMenuItem(title: "Preferences…", action: #selector(Settings.showSettingsWindow), keyEquivalent: "")
    prefs.target = Settings.self
    appMenu.addItem(prefs)
    
    appMenu.addItem(NSMenuItem(title: "Quit", action: Selector("terminate:"), keyEquivalent: ""))
}

func getCharges()
{
    let url = URL(string: "\(Settings.getServer())/api/stats")!
    var request = URLRequest(url: url)
    request.httpMethod = "GET"
    
    NSURLConnection.sendAsynchronousRequest(request, queue: OperationQueue.main) {(response, data, error) in
        guard let data = data else {
            updateMenuBar(users: [])
            return
        }
        
        do {
            let jsonResponse = try JSONSerialization.jsonObject(with: data, options: [])
            users = jsonResponse as! Array<Array<Any>>
            updateMenuBar(users: users)
        } catch {
            updateMenuBar(users: [])
        }
    }
}

func postCharge()
{
    let user = Settings.getName()
    let server = Settings.getServer()
    
    // no submissions while disabled
    if (!enabled) {
        return
    }
    
    // no submissions for blank values
    if (user == "" || server == "") {
        return
    }
    
    let info = getOwnChargeInfo()
    let charging = info.charging
    
    let json = [ "username": user, "percentage": info.percent, "charging": charging] as [String : Any]
    
    let statusString = "[Percent: \(info.percent), charging: \(charging)]"
    
    do {
        let jsonData = try JSONSerialization.data(withJSONObject: json, options: .prettyPrinted)
        
        // create post request
        let url = NSURL(string: "\(Settings.getServer())/percentage")!
        let request = NSMutableURLRequest(url: url as URL)
        request.httpMethod = "POST"
        
        // insert json data to the request
        request.setValue("application/json; charset=utf-8", forHTTPHeaderField: "Content-Type")
        request.httpBody = jsonData
        
        
        let task = URLSession.shared.dataTask(with: request as URLRequest){ data, response, error in
            if error != nil{
                NSLog("Error -> \(error), \(statusString)")
                return
            }
            if let httpResponse = response as? HTTPURLResponse {
                if (httpResponse.statusCode != 200) {
                    // sending failed, TODO: queue up locally
                    NSLog("Did not receive 200 OK from server, \(statusString)")
                }
            }
        }
        
        task.resume()
    } catch {
        NSLog("Some error occurred, \(statusString)")
    }
}

updateMenuTitle()
getCharges()

// update our own battery status locally in the UI every 10 seconds
let dispatchQueue = DispatchQueue(label: "QueueIdentification")
dispatchQueue.async{
    while (true)
    {
        updateMenuTitle()
        sleep(10)
    }
}

// get the charges from the api every 30 seconds
let dispatchQueue2 = DispatchQueue(label: "QueueIdentification")
dispatchQueue2.async{
    while (true)
    {
        getCharges()
        sleep(30)
    }
}

// post our own percent every 60 seconds
let dispatchQueue3 = DispatchQueue(label: "QueueIdentification")
dispatchQueue3.async{
    while (true)
    {
        // sleep until next minute
        let date = Date()
        let seconds = calendar.component(.second, from: date)
        sleep(60 - UInt32(seconds))

        postCharge()
    }
}

if (Settings.getName() == "") {
    // username is blank at launch, display settings
    Settings.showSettingsWindow()
}

NSApp.activate(ignoringOtherApps: true)
NSApp.run()
