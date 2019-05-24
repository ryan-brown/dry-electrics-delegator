package com.dry.electrics

import android.content.Intent
import android.content.IntentFilter
import android.os.BatteryManager
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.dry.electrics.R

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mactivity = this

        batteryStatus = IntentFilter(Intent.ACTION_BATTERY_CHANGED).let { ifilter ->
            this.registerReceiver(null, ifilter)
        }

        getCharges()
    }
}
