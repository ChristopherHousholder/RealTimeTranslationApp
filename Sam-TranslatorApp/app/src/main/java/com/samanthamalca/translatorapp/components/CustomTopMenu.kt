package com.samanthamalca.translatorapp.components

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Person
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.launch

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CustomTopMenu(onMenuClick: () -> Unit) {
    val drawerState = rememberDrawerState(initialValue = DrawerValue.Closed)
    val scope = rememberCoroutineScope()

    ModalNavigationDrawer(
        drawerState = drawerState,
        drawerContent = {
            DrawerContent(onClose = { scope.launch { drawerState.close() } })
        }
    ) {
        // Main Screen Content (your home page design)
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(Color.Black)
        ) {
            // Optional top menu (just the hamburger icon)
            Box(
                modifier = Modifier.fillMaxWidth(),
                contentAlignment = Alignment.TopEnd
            ) {
                IconButton(onClick = { scope.launch { drawerState.open() } }) {
                    Icon(Icons.Default.Person, contentDescription = "Menu", tint = Color.White)
                }
            }

            // Centered circular "button"
            Box(
                modifier = Modifier.fillMaxSize(),
                contentAlignment = Alignment.Center
            ) {
                CircularDesign() // Your circular button here
            }

            // Optional bottom text
            BottomTextField()
        }
    }
}

@Composable
fun DrawerContent(onClose: () -> Unit) {
    Column(
        modifier = Modifier
            .fillMaxHeight()
            .width(280.dp)
            .background(Color(0xFF15202B)) // Dark theme color
            .padding(16.dp),
        horizontalAlignment = Alignment.Start
    ) {
        // Menu Items
        DrawerItem(icon = Icons.Default.Home, text = "Home", onClick = onClose)
        DrawerItem(icon = Icons.Default.Person, text = "Profile", onClick = onClose)
        DrawerItem(icon = Icons.Default.Settings, text = "Settings", onClick = onClose)

        Spacer(modifier = Modifier.height(24.dp))

        // Languages Section
        Text(text = "Languages:", color = Color.White, style = MaterialTheme.typography.bodyLarge)
        Spacer(modifier = Modifier.height(8.dp))
        DrawerItem(icon = Icons.Default.Home, text = "English", onClick = onClose)
        DrawerItem(icon = Icons.Default.Home, text = "Spanish", onClick = onClose)
    }
}

@Composable
fun DrawerItem(icon: androidx.compose.ui.graphics.vector.ImageVector, text: String, onClick: () -> Unit) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(12.dp)
            .clickable { onClick() },
        verticalAlignment = Alignment.CenterVertically
    ) {
        Icon(icon, contentDescription = text, tint = Color.White)
        Spacer(modifier = Modifier.width(12.dp))
        Text(text, color = Color.White, style = MaterialTheme.typography.bodyLarge)
    }
}
