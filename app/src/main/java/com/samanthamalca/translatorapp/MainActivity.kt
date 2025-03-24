package com.samanthamalca.translatorapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.size
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import com.samanthamalca.translatorapp.components.CircularDesign
import com.samanthamalca.translatorapp.components.PulsatingWaves
import com.samanthamalca.translatorapp.components.CustomTopMenu
import com.samanthamalca.translatorapp.components.CurvedLines
//import com.samanthamalca.translatorapp.theme.TranslatorAppTheme
import com.samanthamalca.translatorapp.ui.theme.TranslatorAppTheme
import com.samanthamalca.translatorapp.components.ShazamScreenEffect


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            TranslatorAppTheme {
                MyScreen()
            }
        }
    }
}

@Composable
fun MyScreen() {
    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.Black)
    ) {
        // Add top curved lines
        // I AM COMMENTING THE LINES BECAUSE I NEED TO IMPROVE THEM
//        Box(modifier = Modifier.fillMaxWidth()) {
//            CurvedLines() // Add CurvedLines component here
//        }
        Box(modifier = Modifier.fillMaxSize()) {
            ShazamScreenEffect()
        }

        // Add top menu icon
        Box(modifier = Modifier.fillMaxWidth(), contentAlignment = Alignment.TopEnd) {
            CustomTopMenu(
                { println("Menu Clicked!") }
            ) // Add CustomTopMenu component here
        }

        // Add circular design at center
        Box(
            modifier = Modifier.fillMaxSize(),
            contentAlignment = Alignment.Center
        ) {
            PulsatingWaves()
        }
    }
}
