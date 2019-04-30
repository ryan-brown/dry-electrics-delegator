import Foundation

class ChargeInfo
{
    var user: String
    var percent: Int
    var color: Color
    var icon: String
    var charging: Int
    
    init()
    {
        user = "N/A"
        percent = 0
        color = Color.clear
        icon = "?"
        charging = -1
    }
    
    // TODO: use dict
    init(user: Array<Any>)
    {
        color = hexStringToColor(hex: user[0] as! String)
        self.user = user[1] as! String;
        percent = user[2] as! Int;
        icon = user[3] as! String;
        charging = -1
    }
}
