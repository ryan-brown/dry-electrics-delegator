import Foundation
import Cocoa

func hexStringToNSColor (hex:String) -> NSColor {
    var cString:String = hex.trimmingCharacters(in: .whitespacesAndNewlines).uppercased()
    
    if (cString.hasPrefix("#")) {
        cString.remove(at: cString.startIndex)
    }
    
    if ((cString.count) != 6) {
        return NSColor.gray
    }
    
    var rgbValue:UInt32 = 0
    Scanner(string: cString).scanHexInt32(&rgbValue)
    
    return NSColor(
        red: CGFloat((rgbValue & 0xFF0000) >> 16) / 255.0,
        green: CGFloat((rgbValue & 0x00FF00) >> 8) / 255.0,
        blue: CGFloat(rgbValue & 0x0000FF) / 255.0,
        alpha: CGFloat(1.0)
    )
}

class ChargeInfo
{
    var user: String
    var percent: Int
    var color: NSColor
    var icon: String
    
    // TODO: use dict
    init(user: Array<Any>)
    {
        color = hexStringToNSColor(hex: user[0] as! String)
        self.user = user[1] as! String;
        percent = user[2] as! Int;
        icon = user[3] as! String;
    }
}
