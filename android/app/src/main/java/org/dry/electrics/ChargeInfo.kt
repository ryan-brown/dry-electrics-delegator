package com.dry.electrics

import android.graphics.Color
import org.json.JSONArray

class ChargeInfo(user: JSONArray)
{
    var user: String
    var percent: Int
    var color: Int
    var icon: String
    var charging: Int

    init
    {
        this.user = "N/A"
        percent = 0
        color = Color.TRANSPARENT
        icon = "?"
        charging = -1

        if (user.length() >= 4) {
            color = hexStringToColor(user.getString(0))
            this.user = user.getString(1)
            percent = user.getInt(2)
            icon = user.getString(3)
            charging = -1
        }
    }
}