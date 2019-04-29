import Foundation
import Cocoa

class ChargeInfo
{
    var user: String
    var percent: Int
    var color: NSColor
    var icon: String
    var charging: Int
    
    init()
    {
        user = "N/A"
        percent = 0
        color = NSColor.clear
        icon = "?"
        charging = -1
    }
    
    // TODO: use dict
    init(user: Array<Any>)
    {
        color = hexStringToNSColor(hex: user[0] as! String)
        self.user = user[1] as! String;
        percent = user[2] as! Int;
        icon = user[3] as! String;
        charging = -1
    }
}
