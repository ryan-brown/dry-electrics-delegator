import Foundation
import AppKit
import Cocoa

// initialize the application
NSApplication.shared

// hide the dock icon (same as LSUIElement true in Info.plist)
NSApp.setActivationPolicy(.accessory)

var app = NSApplication.shared
var menuBar = NSMenu()

var appMenu = NSMenu()

let statusItem = NSStatusBar.system.statusItem(withLength: NSStatusItem.variableLength)
statusItem.menu = appMenu

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
    reporting.state = enabled ? NSControl.StateValue.on :  NSControl.StateValue.off
    appMenu.addItem(reporting)
    
    let prefs = NSMenuItem(title: "Preferences…", action: #selector(Settings.showSettingsWindow), keyEquivalent: "")
    prefs.target = Settings.self
    appMenu.addItem(prefs)
    
    appMenu.addItem(NSMenuItem(title: "Quit", action: Selector("terminate:"), keyEquivalent: ""))
}

updateMenuTitle()
getCharges()

updateUI(users: [])
startAsyncThreads()

if (Settings.getZapToken() == "") {
    // username is blank at launch, display settings
    DispatchQueue.main.async {
        Settings.showSettingsWindow()
    }
}

NSApp.activate(ignoringOtherApps: true)
NSApp.run()
