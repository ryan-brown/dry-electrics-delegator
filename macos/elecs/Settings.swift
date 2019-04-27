//
//  Settings.swift
//  Elecs
//
//  Created by Ricky on 4/27/19.
//

import Foundation

class Settings
{
    @objc static func toggleReporting()
    {
        enabled = !enabled
        updateMenuBar(users: users)
    }
}
