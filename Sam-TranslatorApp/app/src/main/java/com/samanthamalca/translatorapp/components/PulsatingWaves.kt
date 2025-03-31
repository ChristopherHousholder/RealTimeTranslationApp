package com.samanthamalca.translatorapp.components

import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp

@Composable
fun PulsatingWaves(
    isPressed: Boolean,
    modifier: Modifier = Modifier
) {
    // Only animate if pressed:
    if (isPressed) {
        val infiniteTransition = rememberInfiniteTransition(label = "pulses")

        // Animate from 0 to 1 repeatedly:
        val animationProgress by infiniteTransition.animateFloat(
            initialValue = 0.7f,
            targetValue = 1f,
            animationSpec = infiniteRepeatable(
                animation = tween(durationMillis = 900, easing = FastOutSlowInEasing),
                repeatMode = RepeatMode.Reverse
            ),
            label = "waveProgress"
        )

        Canvas(modifier = modifier.size(200.dp)) {
            val center = Offset(size.width / 2, size.height / 2)
            // Three concentric waves
//            for (i in 1..3) {
                val i = 3;
                drawCircle(
                    color = Color(0xFFC5C5C5).copy(alpha = 0.4f - (i * 0.1f)),
                    radius = (size.minDimension / 2) * animationProgress * (i * 0.5f),
                    center = center
                )
//            }
        }
    }
}
