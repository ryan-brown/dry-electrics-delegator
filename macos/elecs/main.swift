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
statusItem.title = "\(getPercent())% ⚡️"
statusItem.menu = appMenu

var enabled = true

let utils = Utils()
var users = [[]]

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
        let curUserButton = NSMenuItem(title: view.summary, action: #selector(Utils.toggleReporting), keyEquivalent: "")
        curUserButton.view = view
        curUserButton.target = Utils.self
        appMenu.addItem(curUserButton)
    }

    let reporting = NSMenuItem(title: "Report Charge", action:#selector(Utils.toggleReporting), keyEquivalent: "")
    reporting.target = Utils.self
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

getCharges()

NSApp.activate(ignoringOtherApps: true)
NSApp.run()
