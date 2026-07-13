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
 * gts8wifi: sec_ts touchscreen + S Pen (sec_epen); no hardware touch
 * keys. Sub-services self-check support against tsp cmd_list / node
 * presence.
 */
#define TSP_CMD_NODE "/sys/class/sec/tsp/cmd"
#define TSP_CMD_LIST_NODE "/sys/class/sec/tsp/cmd_list"
#define TSP_CMD_RESULT_NODE "/sys/class/sec/tsp/cmd_result"
#define KEY_DISABLER_NODE "/sys/class/sec/sec_touchkey/input/enabled"
#define EPEN_GESTURE_NODE "/sys/class/sec/sec_epen/epen_gesture"
