package com.dry.electrics

import android.os.BatteryManager
import org.json.JSONArray

fun getOwnChargeInfo(): ChargeInfo {
    val cinfo = ChargeInfo(JSONArray())

    // How are we charging?
    val chargePlug: Int = batteryStatus?.getIntExtra(BatteryManager.EXTRA_PLUGGED, -1) ?: -1
    val usbCharge: Boolean = chargePlug == BatteryManager.BATTERY_PLUGGED_USB
    val acCharge: Boolean = chargePlug == BatteryManager.BATTERY_PLUGGED_AC

    val batteryLevel: Float = batteryStatus?.let { intent ->
        val level: Int = intent.getIntExtra(BatteryManager.EXTRA_LEVEL, -1)
        val scale: Int = intent.getIntExtra(BatteryManager.EXTRA_SCALE, -1)

        level / scale.toFloat()
    } ?: 0f

    cinfo.percent = (batteryLevel * 100).toInt()

    val charging = acCharge || usbCharge

    cinfo.icon = if (charging) "⚡️" else "🔋"
    if (!charging && cinfo.percent < 20) {
        cinfo.icon = "🧧"
    }
    cinfo.charging = if (charging) 1 else 0

    return cinfo
}
