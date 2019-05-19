package org.dry.electrics

import android.content.Intent
import android.graphics.Color
import android.os.BatteryManager
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley

fun hexStringToColor(hex: String): Int {
    return Color.parseColor(hex)
}

var mactivity: MainActivity? = null
var batteryStatus: Intent? = null

fun getCharges()
{
    val queue = Volley.newRequestQueue(mactivity)
    val url = "${Settings.getServer()}/api/stats"

    // Request a string response from the provided URL.
    val stringRequest = StringRequest(
        Request.Method.GET, url,
        Response.Listener<String> { response ->
            println(response)
        },
        Response.ErrorListener {
           println("Some error occurred")
        })

    // Add the request to the RequestQueue.
    queue.add(stringRequest)
}