import Foundation

import IOKit.ps
import AppKit

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
                if (!charging && cinfo.percent < 20) {
                    cinfo.icon = "🧧"
                }
                cinfo.charging = charging ? 1 : 0
            }
        }
    } catch {
    }
    
    return cinfo
}
