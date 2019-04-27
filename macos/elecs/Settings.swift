//
//  Settings.swift
//  Elecs
//
//  Created by Ricky on 4/27/19.
//

import Foundation
import AdSupport

class Settings
{
    var adid = "Unknown Name"
    init() {
        if #available(OSX 10.14, *) {
            if let uuid = ASIdentifierManager.shared().advertisingIdentifier
            {
                adid = uuid.uuidString
            }
        }
    }
    @objc static func toggleReporting()
    {
        enabled = !enabled
        updateMenuBar(users: users)
    }
    
    func updateName(name: String) {
        let defaults = UserDefaults.standard
        defaults.set(name, forKey: "name")
    }
    
    func getName() -> String {
        let defaults = UserDefaults.standard
        return defaults.string(forKey: "name") ?? adid
    }
}
