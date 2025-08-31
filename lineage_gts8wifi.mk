#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_tablet_wifionly.mk)

# Inherit from gts8wifi device
$(call inherit-product, device/samsung/gts8wifi/device.mk)

PRODUCT_DEVICE := gts8wifi
PRODUCT_NAME := lineage_gts8wifi
PRODUCT_BRAND := samsung
PRODUCT_MODEL := SM-X700
PRODUCT_MANUFACTURER := samsung

PRODUCT_GMS_CLIENTID_BASE := android-samsung-ss

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="gts8wifixx-user 15 AP3A.240905.015.A2 X700XXS9DYF4 release-keys" \
    BuildFingerprint=samsung/gts8wifixx/gts8wifi:15/AP3A.240905.015.A2/X700XXS9DYF4:user/release-keys \
    DeviceProduct=gts8wifi \
    SystemName=gts8wifi
