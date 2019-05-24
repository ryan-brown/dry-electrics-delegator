import Foundation

#if os(iOS)
import UIKit
#endif

var users = [[]]

var enabled = true
let settings = Settings()

enum BatteryError: Error { case error }

let calendar = Calendar.current

extension StringProtocol {
    var firstUppercased: String {
        return prefix(1).uppercased() + dropFirst()
    }
    var firstCapitalized: String {
        return String(prefix(1)).capitalized + dropFirst()
    }
}

func hexStringToColor (hex:String) -> Color {
    var cString:String = hex.trimmingCharacters(in: .whitespacesAndNewlines).uppercased()
    
    if (cString.hasPrefix("#")) {
        cString.remove(at: cString.startIndex)
    }
    
    if ((cString.count) != 6) {
        return Color.gray
    }
    
    var rgbValue:UInt32 = 0
    Scanner(string: cString).scanHexInt32(&rgbValue)
    
    return Color(
        red: CGFloat((rgbValue & 0xFF0000) >> 16) / 255.0,
        green: CGFloat((rgbValue & 0x00FF00) >> 8) / 255.0,
        blue: CGFloat(rgbValue & 0x0000FF) / 255.0,
        alpha: CGFloat(1.0)
    )
}

func getCharges()
{
    let url = URL(string: "\(Settings.getServer())/api/stats")!
    var request = URLRequest(url: url)
    request.httpMethod = "GET"
    
    NSURLConnection.sendAsynchronousRequest(request, queue: OperationQueue.main) {(response, data, error) in
        guard let data = data else {
            updateUI(users: [])
            return
        }
        
        do {
            let jsonResponse = try JSONSerialization.jsonObject(with: data, options: [])
            users = jsonResponse as! Array<Array<Any>>
            updateUI(users: users)
        } catch {
            updateUI(users: [])
        }
    }
}

func postCharge()
{
    let zap_token = Settings.getZapToken()
    let server = Settings.getServer()
    
    // no submissions while disabled
    if (!enabled) {
        return
    }
    
    // no submissions for blank values
    if (zap_token == "" || server == "") {
        return
    }
    
    let info = getOwnChargeInfo()
    let charging = info.charging
    
    let json = [ "zap_token": zap_token, "percentage": info.percent, "charging": charging] as [String : Any]
    
    let statusString = "[Percent: \(info.percent), charging: \(charging)]"
    
    do {
        let jsonData = try JSONSerialization.data(withJSONObject: json, options: .prettyPrinted)
        
        // create post request
        let url = NSURL(string: "\(Settings.getServer())/percentage")!
        let request = NSMutableURLRequest(url: url as URL)
        request.httpMethod = "POST"
        
        // insert json data to the request
        request.setValue("application/json; charset=utf-8", forHTTPHeaderField: "Content-Type")
        request.httpBody = jsonData
        
        
        let task = URLSession.shared.dataTask(with: request as URLRequest){ data, response, error in
            if error != nil{
                NSLog("Error -> \(error), \(statusString)")
                return
            }
            if let httpResponse = response as? HTTPURLResponse {
                if (httpResponse.statusCode != 200) {
                    // sending failed, TODO: queue up locally
                    NSLog("Did not receive 200 OK from server, \(statusString)")
                }
            }
        }
        
        task.resume()
    } catch {
        NSLog("Some error occurred, \(statusString)")
    }
}

func startAsyncThreads()
{
    
    // update our own battery status locally in the UI every 10 seconds
    let dispatchQueue = DispatchQueue(label: "QueueIdentification")
    dispatchQueue.async{
        while (true)
        {
            updateOurCharge()
            sleep(10)
        }
    }
    
    // get the charges from the api every 30 seconds
    let dispatchQueue2 = DispatchQueue(label: "QueueIdentification")
    dispatchQueue2.async{
        while (true)
        {
            getCharges()
            sleep(30)
        }
    }
    
    // post our own percent every 60 seconds
    let dispatchQueue3 = DispatchQueue(label: "QueueIdentification")
    dispatchQueue3.async{
        while (true)
        {
            // sleep until next frequency (default 60 min)
            let date = Date()
            let seconds = calendar.component(.second, from: date)
            
            let freq = UInt32(Settings.getFrequency())
            sleep(freq - (UInt32(seconds) % freq))
            
            postCharge()
        }
    }
}

#if os(macOS)
class OnlyIntegerValueFormatter: NumberFormatter {
    
    override func isPartialStringValid(_ partialString: String, newEditingString newString: AutoreleasingUnsafeMutablePointer<NSString?>?, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool {
        
        // Ability to reset your field (otherwise you can't delete the content)
        // You can check if the field is empty later
        if partialString.isEmpty {
            return true
        }
        
        // Actual check
        return Int(partialString) != nil
    }
}
#endif
