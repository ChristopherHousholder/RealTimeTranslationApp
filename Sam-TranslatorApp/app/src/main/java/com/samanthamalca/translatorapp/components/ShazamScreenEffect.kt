package com.samanthamalca.translatorapp.components

import androidx.compose.animation.core.*
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color

@Composable
fun ShazamScreenEffect() {
    val infiniteTransition = rememberInfiniteTransition(label = "infinite")

    // Create two ripple animations that expand from the center
    val ripples = List(2) { index ->
        infiniteTransition.animateFloat(
            initialValue = 0f,
            targetValue = 1.2f,  // Allows the ripple to expand beyond its normal radius
            animationSpec = infiniteRepeatable(
                animation = tween(durationMillis = 1500, easing = LinearEasing),
                repeatMode = RepeatMode.Restart
            ),
            label = "ripple$index"
        )
    }

    Box(
        modifier = Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        Canvas(modifier = Modifier.fillMaxSize()) {
            val center = Offset(size.width / 2, size.height / 2)
            val maxRadius = size.width * 0.5f

            ripples.forEach { ripple ->
                // Clamping the alpha to ensure it never goes below 0
                val currentAlpha = (1f - ripple.value).coerceIn(0f, 1f)

                drawCircle(
                    color = Color.White.copy(alpha = currentAlpha),
                    radius = maxRadius * ripple.value,
                    center = center
                )
            }
        }
    }
}