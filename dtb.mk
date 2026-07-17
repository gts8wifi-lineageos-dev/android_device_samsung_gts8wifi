#
# Copyright (C) 2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

GTS8WIFI_DTB_DIR := $(DTB_OUT)/arch/$(KERNEL_ARCH)/boot/dts/vendor/qcom
GTS8WIFI_DTB_NAMES := \
    waipio-v2.dtb \
    waipio.dtb \
    waipiop-v2.dtb \
    waipiop.dtb
GTS8WIFI_DTB_FILES := $(addprefix $(GTS8WIFI_DTB_DIR)/,$(GTS8WIFI_DTB_NAMES))
GTS8WIFI_DTB_SRCS := $(addprefix $(KERNEL_SRC)/arch/$(KERNEL_ARCH)/boot/dts/vendor/qcom/,$(GTS8WIFI_DTB_NAMES:.dtb=.dts))

GTS8WIFI_DTB_SRCS += $(wildcard \
    $(KERNEL_SRC)/arch/$(KERNEL_ARCH)/boot/dts/vendor/qcom/*.dtsi)

$(DTB_OUT):
	mkdir -p $@

$(INSTALLED_DTBIMAGE_TARGET): $(DTC) $(GTS8WIFI_DTB_SRCS) | $(DTB_OUT)
	@echo "Building gts8wifi dtb.img from source"
	$(call make-kernel-config,$(DTB_OUT),$(ALL_KERNEL_DEFCONFIG_SRCS))
	$(call make-dtb-target,$(TARGET_KERNEL_DTB))
	$(hide) for dtb in $(GTS8WIFI_DTB_FILES); do \
		test -f $$dtb || { echo "Missing DTB: $$dtb"; exit 1; }; \
	done
	$(hide) rm -f $@
	$(hide) cat $(GTS8WIFI_DTB_FILES) > $@
	$(hide) touch -c $(DTB_OUT)
