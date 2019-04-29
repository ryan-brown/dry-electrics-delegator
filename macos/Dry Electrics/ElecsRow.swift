//
//  ElecsView.swift
//  Elecs
//
//  Created by Ricky on 4/26/19.
//

import Foundation
import AppKit

class ElecsRow : NSTextField
{
    let summary: String
    let username: String
    
    init(_ info: ChargeInfo)
    {
        let frame = CGRect(origin: .zero, size: CGSize(width: 150, height: 26))
        
        username = info.user
        
        summary = "\(info.icon) \(info.user): \(info.percent)%"

        super.init(frame: frame)
        
        self.wantsLayer = true
        self.layer?.backgroundColor = info.color.cgColor

        self.font = NSFont.systemFont(ofSize: 14)
//        self.font = NSFont(name: "Raleway-Regular", size: 18)
        self.isEditable = false
        self.textColor = NSColor.black
        self.stringValue = summary
        
    }
    
    override func mouseDown(with theEvent : NSEvent) {
        if let url = URL(string: "\(Settings.getServer())/users/\(username)") {
            NSWorkspace.shared.open(url)
        }
    }
    
    required init?(coder decoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    // https://stackoverflow.com/a/27448397
    override var allowsVibrancy: Bool { return false }

}
