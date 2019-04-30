import Foundation

import UIKit

func getOwnChargeInfo() -> ChargeInfo
{
    let cinfo = ChargeInfo()

    var batteryLevel: Float {
        return UIDevice.current.batteryLevel
    }
    
    var batteryState: UIDevice.BatteryState {
        return UIDevice.current.batteryState
    }
    
    cinfo.percent = Int(batteryLevel * 100)
    
    let chargingState = batteryState
    let charging = chargingState == .charging || chargingState == .full
    
    cinfo.icon = charging ? "⚡️" : "🔋"
    if (!charging && cinfo.percent < 20) {
        cinfo.icon = "🧧"
    }
    cinfo.charging = charging ? 1 : 0
    
    return cinfo
}

func updateTable(users: Array<Array<Any>>) {
    
    if let textArea = ViewController.textArea {
        var content = ""
        
        for user in users
        {
            let info = ChargeInfo(user: user)
            content += "\(info.icon) \(info.user): \(info.percent)%\n"
        }
        
        textArea.text = content
    }
}
