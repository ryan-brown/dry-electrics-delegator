import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var userField: UITextField!
    
    @IBOutlet weak var serverField: UITextField!
    
    @IBOutlet weak var textArea: UITextView!
    
    @IBAction func updateClick(_ sender: Any) {
        Settings.setZapToken(token: userField.text ?? "")
        Settings.setServer(server: serverField.text ?? "")
    }
    
    static var textArea: UITextView? = nil
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        ViewController.textArea = textArea
        
        userField.text = Settings.getZapToken()
        serverField.text = Settings.getServer()
    UIDevice.current.isBatteryMonitoringEnabled = true
        
        updateOurCharge()
        getCharges()
        
        startAsyncThreads()
    }
}
