#
# Copyright (C) 2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

MKDTBOIMG := $(HOST_OUT_EXECUTABLES)/mkdtboimg$(HOST_EXECUTABLE_SUFFIX)

GTS8WIFI_DTBO_DIR := $(DTBO_OUT)/arch/$(KERNEL_ARCH)/boot/dts/samsung/galaxytab/gts8wifi
GTS8WIFI_DTBO_NAMES := \
    gts8wifi_chn_open_w00_r04.dtbo \
    gts8wifi_chn_open_w00_r05.dtbo \
    gts8wifi_chn_open_w00_r06.dtbo \
    gts8wifi_chn_open_w00_r07.dtbo \
    gts8wifi_chn_open_w00_r08.dtbo
GTS8WIFI_DTBO_FILES := $(addprefix $(GTS8WIFI_DTBO_DIR)/,$(GTS8WIFI_DTBO_NAMES))
GTS8WIFI_DTBO_SRCS := $(addprefix $(KERNEL_SRC)/arch/$(KERNEL_ARCH)/boot/dts/samsung/galaxytab/gts8wifi/,$(GTS8WIFI_DTBO_NAMES:.dtbo=.dts))

$(DTBO_OUT):
	mkdir -p $@

$(BOARD_PREBUILT_DTBOIMAGE): $(DTC) $(MKDTBOIMG) $(GTS8WIFI_DTBO_SRCS) | $(DTBO_OUT)
	@echo "Building gts8wifi dtbo.img from source"
	$(call make-dtbo-target,$(KERNEL_DEFCONFIG))
	$(call make-dtbo-target,$(TARGET_KERNEL_DTB))
	$(hide) for dtbo in $(GTS8WIFI_DTBO_FILES); do \
		test -f $$dtbo || { echo "Missing DTBO: $$dtbo"; exit 1; }; \
	done
	$(MKDTBOIMG) create $@ --page_size=$(BOARD_KERNEL_PAGESIZE) $(GTS8WIFI_DTBO_FILES)
