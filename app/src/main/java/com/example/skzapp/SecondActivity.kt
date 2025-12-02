package com.example.skzapp

import android.graphics.Color
import android.os.Bundle
import android.text.SpannableString
import android.text.Spanned
import android.text.style.ForegroundColorSpan
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class SecondActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_page_greetings)

        val tvTitle = findViewById<TextView>(R.id.tvTitle)
        val titleText = SpannableString("I am goose Goosely")
        val orangeColor = Color.parseColor("#EC9E51")
        titleText.setSpan(
            ForegroundColorSpan(orangeColor),
            11,
            18,
            Spanned.SPAN_EXCLUSIVE_EXCLUSIVE
        )
        tvTitle.text = titleText

        val tvDescription = findViewById<TextView>(R.id.tvDescription)
        val descText = SpannableString("I am an assistant on your way to a healthy lifestyle.")
        descText.setSpan(
            ForegroundColorSpan(orangeColor),
            46,
            55,
            Spanned.SPAN_EXCLUSIVE_EXCLUSIVE
        )
        tvDescription.text = descText

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
    }
}