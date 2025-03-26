package com.samanthamalca.translatorapp.components


import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.size
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.unit.dp

@Composable
fun CircularDesign() {
    var isPressed by remember { mutableStateOf(false) }

    val scale by animateFloatAsState(
        targetValue = if (isPressed) 1.2f else 1f,
        animationSpec = tween(durationMillis = 300)
    )

    val rotation by animateFloatAsState(
        targetValue = if (isPressed) 15f else 0f,
        animationSpec = tween(durationMillis = 300)
    )

    Canvas(
        modifier = Modifier
            .size(200.dp)
            .clickable { isPressed = !isPressed }
            .graphicsLayer(scaleX = scale, scaleY = scale, rotationZ = rotation)
    ) {
        val center = Offset(size.width / 2, size.height / 2)
        val colorsLeft = listOf(
            Color(0xFF121230), Color(0xFF1D1D5E),
            Color(0xFF2E2E90), Color(0xFF4A4AD3),
            Color(0xFFB0B0FF), Color(0xFFD8D8FF)
        )

        val colorsRight = listOf(
            Color(0xFF0E0E25), Color(0xFF18184A),
            Color(0xFF25257A), Color(0xFF3939B0),
            Color(0xFF8C8CFF), Color(0xFFC0C0FF)
        )

        val radiusStep = size.minDimension / 2 / colorsLeft.size
        colorsLeft.forEachIndexed { index, color ->
            drawArc(
                color = color,
                startAngle = 90f,
                sweepAngle = 180f,
                useCenter = true,
                topLeft = Offset(center.x - radiusStep * (colorsLeft.size - index), center.y - radiusStep * (colorsLeft.size - index)),
                size = androidx.compose.ui.geometry.Size(radiusStep * (colorsLeft.size - index) * 2, radiusStep * (colorsLeft.size - index) * 2)
            )
        }

        colorsRight.forEachIndexed { index, color ->
            drawArc(
                color = color,
                startAngle = -90f,
                sweepAngle = 180f,
                useCenter = true,
                topLeft = Offset(center.x - radiusStep * (colorsRight.size - index), center.y - radiusStep * (colorsRight.size - index)),
                size = androidx.compose.ui.geometry.Size(radiusStep * (colorsRight.size - index) * 2, radiusStep * (colorsRight.size - index) * 2)
            )
        }
    }
}
