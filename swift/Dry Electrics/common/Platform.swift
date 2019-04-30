// this file renames some platform-specific stuff to common versions
import Foundation

#if os(iOS)
import UIKit
typealias Color = UIColor
#else
import AppKit
typealias Color = NSColor
#endif

func updateUI(users: Array<Array<Any>>) {
    #if os(macOS)
    updateMenuBar(users: users)
    #else
    updateTable(users: users)
    #endif
}

func updateOurCharge() {
    #if os(macOS)
        updateMenuTitle()
    #else

    #endif
}
