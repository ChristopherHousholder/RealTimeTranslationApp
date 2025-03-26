package com.samanthamalca.translatorapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.size
import androidx.compose.material3.Surface
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.samanthamalca.translatorapp.components.BottomTextField
import com.samanthamalca.translatorapp.components.CustomTopMenu
import com.samanthamalca.translatorapp.components.PulsatingWaves
import com.samanthamalca.translatorapp.components.ShazamScreenEffect
import com.samanthamalca.translatorapp.ui.theme.TranslatorAppTheme

@Composable
fun MyScreen() {
    // State variable to track whether the ripple effect is active
    var isEffectActive by remember { mutableStateOf(false) }

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.Black)
    ) {
        // Conditionally show the Shazam-like ripple effect
        if (isEffectActive) {
            Box(modifier = Modifier.fillMaxSize()) {
                ShazamScreenEffect()
            }
        }

        // Top menu icon
        Box(modifier = Modifier.fillMaxWidth(), contentAlignment = Alignment.TopEnd) {
            CustomTopMenu { println("Menu Clicked!") }
        }

        // Central circle button that toggles the ripple effect
        Box(
            modifier = Modifier
                .size(100.dp) // Adjust the size as needed
                .align(Alignment.Center)
                .clickable { isEffectActive = !isEffectActive },
            contentAlignment = Alignment.Center
        ) {
            PulsatingWaves()
        }

        // Bottom text field
        BottomTextField()
    }
}

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
