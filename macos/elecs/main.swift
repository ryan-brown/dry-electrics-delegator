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
    
    appMenu.addItem(NSMenuItem(title: "Preferences…", action: Selector("terminate:"), keyEquivalent: ""))
    
    appMenu.addItem(NSMenuItem(title: "Quit", action: Selector("terminate:"), keyEquivalent: ""))
}

func getCharges()
{
    let url = URL(string: "https://electrics.fortheusers.org/api/stats")!
    var request = URLRequest(url: url)
    request.httpMethod = "GET"
    
    NSURLConnection.sendAsynchronousRequest(request, queue: OperationQueue.main) {(response, data, error) in
        guard let data = data else { return }
        
        do {
            let jsonResponse = try JSONSerialization.jsonObject(with: data, options: [])
            users = jsonResponse as! Array<Array<Any>>
            updateMenuBar(users: users)
        } catch { }
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
        // TODO: this, use username from Settings
        sleep(60)
    }
}

NSApp.activate(ignoringOtherApps: true)
NSApp.run()
