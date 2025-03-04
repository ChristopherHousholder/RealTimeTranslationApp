package com.example.translateapp


import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.material.ripple.rememberRipple
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MyAppUI()
        }
    }
}

@Composable
fun MyAppUI() {
    var buttonColor by remember { mutableStateOf(Color(0xFF7E57C2)) } // Initial purple color
    var isMenuOpen by remember { mutableStateOf(false) } // State for main menu

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(Color(0xFF42A5F5)) // Light Blue Background
    ) {
        Column(
            modifier = Modifier.fillMaxSize(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // Clickable Circle Button with Ripple Effect
            Box(
                modifier = Modifier
                    .size(100.dp)
                    .background(buttonColor, shape = CircleShape)
                    .clickable(
                        interactionSource = remember { MutableInteractionSource() },
                        indication = rememberRipple(bounded = false)
                    ) {
                        // Toggle button color when clicked
                        buttonColor = if (buttonColor == Color(0xFF7E57C2)) Color(0xFFAB47BC) else Color(0xFF7E57C2)
                    }
            )

            Spacer(modifier = Modifier.height(150.dp))

            // Text Box
            Box(
                modifier = Modifier
                    .fillMaxWidth(0.9f)
                    .height(80.dp)
                    .background(Color.Gray, shape = RoundedCornerShape(16.dp)),
                contentAlignment = Alignment.Center
            ) {
                Text("Text Box", fontSize = 20.sp, color = Color.Black)
            }
        }

        // Clickable Main Menu (Three Dots)
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(top = 20.dp, end = 20.dp)
                .clickable(
                    interactionSource = remember { MutableInteractionSource() },
                    indication = rememberRipple(bounded = false)
                ) {
                    isMenuOpen = !isMenuOpen // Toggle menu visibility
                },
            horizontalArrangement = Arrangement.End
        ) {
            repeat(3) {
                Box(
                    modifier = Modifier
                        .size(10.dp)
                        .background(Color.Black, shape = CircleShape)
                        .padding(5.dp)
                )
                Spacer(modifier = Modifier.width(5.dp))
            }
        }

        // Display Menu when clicked
        if (isMenuOpen) {
            Box(
                modifier = Modifier
                    .align(Alignment.TopEnd)
                    .padding(top = 50.dp, end = 20.dp)
                    .background(Color.White, shape = RoundedCornerShape(10.dp))
                    .padding(10.dp)
            ) {
                Text(
                    text = "Menu Opened",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.Black
                )
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun PreviewMyAppUI() {
    MyAppUI()
}
