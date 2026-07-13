/*
 * Copyright (C) 2016 The CyanogenMod Project
 *               2017-2022 The LineageOS Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

/*
 * Board specific nodes
 *
 * gts8wifi: backlight is exposed at panel0-backlight; there is no
 * touchkey backlight or notification LED on this device.
 */
#define PANEL_BRIGHTNESS_NODE "/sys/class/backlight/panel0-backlight/brightness"
#define PANEL_MAX_BRIGHTNESS_NODE "/sys/class/backlight/panel0-backlight/max_brightness"
#define BUTTON_BRIGHTNESS_NODE "/sys/class/sec/sec_touchkey/brightness"
#define LED_BLINK_NODE "/sys/class/sec/led/led_blink"
#define LED_BLN_NODE "/sys/class/misc/backlightnotification/notification_led"

/*
 * Brightness adjustment factors
 */
#define LED_ADJUSTMENT_R 1.0
#define LED_ADJUSTMENT_G 1.0
#define LED_ADJUSTMENT_B 1.0

/*
 * Light brightness factors
 */
#define LED_BRIGHTNESS_BATTERY 255
#define LED_BRIGHTNESS_NOTIFICATION 255
#define LED_BRIGHTNESS_ATTENTION 255
