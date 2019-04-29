//
//  Settings.swift
//  Elecs
//
//  Created by Ricky on 4/27/19.
//

import Foundation
import AdSupport
import AppKit

class Settings
{
    static var window: NSWindow? = nil
    
    static let defaults = UserDefaults.standard
    
    static var defaultUser = ""
    static let defaultServer = "https://electrics.fortheusers.org"
    
    static var userText: NSTextField?
    static var serverText: NSTextField?

    init() {
//        if #available(OSX 10.14, *) {
//            if let uuid = ASIdentifierManager.shared().advertisingIdentifier
//            {
//                Settings.adid = String(uuid.uuidString.split(separator: "-")[0]).lowercased()
//            }
//        }
    }
    @objc static func toggleReporting()
    {
        enabled = !enabled
        updateMenuBar(users: users)
    }
    
    static func setUser(name: String) {
        defaults.set(name, forKey: "name")
    }
    
    static func getName() -> String {
        return defaults.string(forKey: "name") ?? defaultUser
    }
    
    static func setServer(server: String) {
        defaults.set(server, forKey: "server")
    }
    
    static func getServer() -> String {
        return defaults.string(forKey: "server") ?? defaultServer
    }
    
    @objc static func close() {
        if (window != nil) {
            Settings.setUser(name: userText?.stringValue ?? "")
            Settings.setServer(server: serverText?.stringValue ?? "")
            
            let windowCopy = window!
            window = nil
            windowCopy.close()
        }
    }

    @objc static func showSettingsWindow() {
        if Settings.window != nil {
            return
        }
        
        let frameRect = CGRect(origin: .zero, size: CGSize(width: 370, height: 150))
        
        Settings.window = NSWindow(contentRect: frameRect, styleMask: [.titled], backing: .buffered, defer: false)
        
        let window = Settings.window!
        window.isReleasedWhenClosed = false
        window.center()

        let view = NSView()
        
        let userTextLabel = NSTextField()
        userTextLabel.stringValue = "User"
        userTextLabel.isEditable = false
        userTextLabel.drawsBackground = false
        userTextLabel.isBezeled = false
        userTextLabel.frame = CGRect(origin: CGPoint(x: 20, y: 110), size: CGSize(width: 100, height: 25))
        view.addSubview(userTextLabel)
        
        let userText = NSTextField()
        let name = Settings.getName()
        userText.stringValue = name == "" ? NSUserName().firstUppercased : name
        userText.frame = CGRect(origin: CGPoint(x: 80, y: 110), size: CGSize(width: 250, height: 25))
        userText.cell?.wraps = false
        userText.cell?.isScrollable = true
        if #available(OSX 10.10, *) {
            userText.placeholderString = "Username"
        }
        view.addSubview(userText)
        Settings.userText = userText
        
        let nameTextLabel = NSTextField()
        nameTextLabel.stringValue = "Server"
        nameTextLabel.isEditable = false
        nameTextLabel.drawsBackground = false
        nameTextLabel.isBezeled = false
        nameTextLabel.frame = CGRect(origin: CGPoint(x: 20, y: 70), size: CGSize(width: 100, height: 25))
        view.addSubview(nameTextLabel)

        let serverText = NSTextField()
        serverText.stringValue = Settings.getServer()
        serverText.cell?.wraps = false
        serverText.cell?.isScrollable = true
        serverText.frame = CGRect(origin: CGPoint(x: 80, y: 70), size: CGSize(width: 250, height: 25))
        if #available(OSX 10.10, *) {
            serverText.placeholderString = "Org (blank for default)"
        }
        view.addSubview(serverText)
        Settings.serverText = serverText
        
        let save = NSButton()
        save.setButtonType(.momentaryLight)
        save.bezelStyle = .rounded
        save.title = "Save Preferences"
        save.frame = CGRect(origin: CGPoint(x: 120, y: 15), size: CGSize(width: 140, height: 25))
        save.action = #selector(Settings.close)
        save.target = Settings.self
        view.addSubview(save)
        
        view.isHidden = false
        view.needsDisplay = true
        window.contentView = view
        
        window.cascadeTopLeft(from: NSMakePoint(20, 20))
        window.title = "Dry Electrics Preferences"
        window.makeKeyAndOrderFront(nil)
    }
}
