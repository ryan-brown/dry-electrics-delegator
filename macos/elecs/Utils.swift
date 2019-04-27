import Foundation
import IOKit.ps
import AppKit

enum BatteryError: Error { case error }

func getOwnChargeInfo() -> ChargeInfo
{
    let cinfo = ChargeInfo()
    do {
        // Take a snapshot of all the power source info
        guard let snapshot = IOPSCopyPowerSourcesInfo()?.takeRetainedValue()
            else { throw BatteryError.error }
        
        // Pull out a list of power sources
        guard let sources: NSArray = IOPSCopyPowerSourcesList(snapshot)?.takeRetainedValue()
            else { throw BatteryError.error }
        
        // For each power source...
        for ps in sources {
            // Fetch the information for a given power source out of our snapshot
            guard let info: NSDictionary = IOPSGetPowerSourceDescription(snapshot, ps as CFTypeRef)?.takeUnretainedValue()
                else { throw BatteryError.error }
            
            // Pull out the name and current capacity
            if let name = info[kIOPSNameKey] as? String,
                let capacity = info[kIOPSCurrentCapacityKey] as? Double,
                let max = info[kIOPSMaxCapacityKey] as? Double {
                    cinfo.percent = Int(capacity / max * 100)
                }
            if let charging = info[kIOPSIsChargingKey] as? Bool {
                cinfo.icon = charging ? "⚡️" : "🔋"
                if (cinfo.percent < 20) {
                    cinfo.icon = "🧧"
                }
            }
        }
    } catch {
    }
    
    return cinfo
}

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
