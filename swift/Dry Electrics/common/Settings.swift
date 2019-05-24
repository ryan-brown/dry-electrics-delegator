//
//  Settings.swift
//  Elecs
//
//  Created by Ricky on 4/27/19.
//

import Foundation

#if os(macOS)
import AppKit
#endif

class Settings
{
    static let defaults = UserDefaults.standard
    
    static var defaultZapToken = ""
    static let defaultServer = "https://electrics.fortheusers.org"
    static let defaultFrequency = 30

    init() {
    }
    
    static func setZapToken(token: String) {
        defaults.set(token, forKey: "zap_token")
    }
    
    static func getZapToken() -> String {
        return defaults.string(forKey: "zap_token") ?? defaultZapToken
    }
    
    static func setServer(server: String) {
        defaults.set(server, forKey: "server")
    }
    
    static func getServer() -> String {
        if let value = defaults.string(forKey: "server") {
            if value == "" {
                return defaultServer
            }
            return value
        }
        
        return defaultServer
    }
    
    static func setFrequency(server: Int) {
        if server > 0 && server <= 60 {
            defaults.set(server, forKey: "push_freq")
        }
    }
    
    static func getFrequency() -> Int {
        let value = defaults.integer(forKey: "push_freq")
        
        if value < 1 || value > 60 {
            return defaultFrequency
        }
        
        return defaults.integer(forKey: "push_freq")
    }
    
    #if os(macOS)
    
    class MTextField: NSTextField {
        
        private let commandKey = NSEvent.ModifierFlags.command.rawValue
        private let commandShiftKey = NSEvent.ModifierFlags.command.rawValue | NSEvent.ModifierFlags.shift.rawValue
        
        override func performKeyEquivalent(with event: NSEvent) -> Bool {
            if event.type == NSEvent.EventType.keyDown {
                if (event.modifierFlags.rawValue & NSEvent.ModifierFlags.deviceIndependentFlagsMask.rawValue) == commandKey {
                    switch event.charactersIgnoringModifiers! {
                    case "x":
                        if NSApp.sendAction(#selector(NSText.cut(_:)), to:nil, from:self) { return true }
                    case "c":
                        if NSApp.sendAction(#selector(NSText.copy(_:)), to:nil, from:self) { return true }
                    case "v":
                        if NSApp.sendAction(#selector(NSText.paste(_:)), to:nil, from:self) { return true }
                    case "z":
                        if NSApp.sendAction(Selector(("undo:")), to:nil, from:self) { return true }
                    case "a":
                        if NSApp.sendAction(#selector(NSResponder.selectAll(_:)), to:nil, from:self) { return true }
                    default:
                        break
                    }
                }
                else if (event.modifierFlags.rawValue & NSEvent.ModifierFlags.deviceIndependentFlagsMask.rawValue) == commandShiftKey {
                    if event.charactersIgnoringModifiers == "Z" {
                        if NSApp.sendAction(Selector(("redo:")), to:nil, from:self) { return true }
                    }
                }
            }
            return super.performKeyEquivalent(with: event)
        }
        
    }
    
    static var window: NSWindow? = nil
    
    static var userText: MTextField?
    static var serverText: MTextField?
    static var frequencyText: MTextField?
    
    @objc static func toggleReporting()
    {
        enabled = !enabled
        updateMenuBar(users: users)
    }
    
    @objc static func close() {
        if (window != nil) {
            Settings.setZapToken(token: userText?.stringValue ?? "")
            Settings.setServer(server: serverText?.stringValue ?? "")
            Settings.setFrequency(server: Int(frequencyText?.intValue ?? 0))
            
            let windowCopy = window!
            window = nil
            windowCopy.close()
        }
    }

    @objc static func showSettingsWindow() {
        
        NSApp.activate(ignoringOtherApps: true)
        
        if Settings.window != nil {
            Settings.window?.makeKey()
            return
        }
        
        let frameRect = CGRect(origin: .zero, size: CGSize(width: 370, height: 200))
        
        Settings.window = NSWindow(contentRect: frameRect, styleMask: [.titled], backing: .buffered, defer: false)
        
        let window = Settings.window!
        window.isReleasedWhenClosed = false
        window.center()

        let view = NSView()
        
        let top = 160
        
        let userTextLabel = NSTextField()
        userTextLabel.stringValue = "Zap Token"
        userTextLabel.isEditable = false
        userTextLabel.drawsBackground = false
        userTextLabel.isBezeled = false
        userTextLabel.frame = CGRect(origin: CGPoint(x: 20, y: top), size: CGSize(width: 100, height: 25))
        view.addSubview(userTextLabel)
        
        let userText = MTextField()
        let name = Settings.getZapToken()
        userText.stringValue = name
        userText.frame = CGRect(origin: CGPoint(x: 100, y: top), size: CGSize(width: 230, height: 25))
        userText.cell?.wraps = false
        userText.cell?.isScrollable = true
        if #available(OSX 10.10, *) {
            userText.placeholderString = "Zap Token"
        }
        view.addSubview(userText)
        Settings.userText = userText
        
        let nameTextLabel = NSTextField()
        nameTextLabel.stringValue = "Server"
        nameTextLabel.isEditable = false
        nameTextLabel.drawsBackground = false
        nameTextLabel.isBezeled = false
        nameTextLabel.frame = CGRect(origin: CGPoint(x: 20, y: top - 40), size: CGSize(width: 100, height: 25))
        view.addSubview(nameTextLabel)

        let serverText = MTextField()
        serverText.stringValue = Settings.getServer()
        serverText.cell?.wraps = false
        serverText.cell?.isScrollable = true
        serverText.frame = CGRect(origin: CGPoint(x: 100, y: top - 40), size: CGSize(width: 230, height: 25))
        if #available(OSX 10.10, *) {
            serverText.placeholderString = "Server"
        }
        view.addSubview(serverText)
        Settings.serverText = serverText
        
        let intervalLabel = NSTextField()
        intervalLabel.stringValue = "Submit battery data every          seconds"
        intervalLabel.isEditable = false
        intervalLabel.drawsBackground = false
        intervalLabel.isBezeled = false
        intervalLabel.frame = CGRect(origin: CGPoint(x: 50, y: top - 90), size: CGSize(width: 300, height: 25))
        view.addSubview(intervalLabel)
        
        frequencyText = MTextField()
        let interval = frequencyText!
        let onlyIntFormatter = OnlyIntegerValueFormatter()
        interval.formatter = onlyIntFormatter
        interval.stringValue = "\(Settings.getFrequency())"
        interval.frame = CGRect(origin: CGPoint(x: 204, y: top - 85), size: CGSize(width: 25, height: 25))
        view.addSubview(interval)
        
        let save = NSButton()
        save.setButtonType(.momentaryLight)
        save.bezelStyle = .rounded
        save.title = "Save Preferences"
        save.frame = CGRect(origin: CGPoint(x: 130, y: top - 130), size: CGSize(width: 140, height: 25))
        save.action = #selector(Settings.close)
        save.target = Settings.self
        view.addSubview(save)
        
        view.isHidden = false
        view.needsDisplay = true
        window.contentView = view
        
        window.cascadeTopLeft(from: NSMakePoint(20, 20))
        window.title = "Dry Electrics Preferences"
        window.makeKeyAndOrderFront(nil)
        
        window.makeKey()
    }
    #endif
}
