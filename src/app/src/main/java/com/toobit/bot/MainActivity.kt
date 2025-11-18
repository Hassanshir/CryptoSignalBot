package com.toobit.bot

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.coroutines.*
import okhttp3.OkHttpClient
import okhttp3.Request
import org.json.JSONObject
import android.widget.TextView

class MainActivity : AppCompatActivity() {

    private val client = OkHttpClient()
    private lateinit var txt: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        txt = TextView(this)
        setContentView(txt)

        fetchVolumeAlerts()
    }

    private fun fetchVolumeAlerts() {
        GlobalScope.launch(Dispatchers.IO) {
            val request = Request.Builder()
                .url("https://api.toobit.com/quote/v1/tickers")
                .build()

            val response = client.newCall(request).execute().body?.string()
            if (response != null) {
                val json = JSONObject(response)
                val data = json.getJSONArray("data")

                var result = ""
                for (i in 0 until data.length()) {
                    val obj = data.getJSONObject(i)
                    val symbol = obj.getString("symbol")
                    val volume = obj.getDouble("volume")
                    if (volume > 5000000) {
                        result += "$symbol → Volume: $volume\n"
                    }
                }

                withContext(Dispatchers.Main) {
                    txt.text = result.ifEmpty { "No high volume detected." }
                }
            }
        }
    }
}
