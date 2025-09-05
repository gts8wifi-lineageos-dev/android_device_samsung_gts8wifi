#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/samsung/gts8wifi',
    'vendor/qcom/opensource/display',
    'hardware/qcom-caf/sm8450',
    'vendor/qcom/opensource/dataservices',
    'hardware/qcom-caf/wlan',
    'hardware/qcom/wlan/legacy',
]

# Lib fixups
def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
    ): lib_fixup_vendor_suffix,
    (
        'libagm',
        'libagmclient',
        'libagmmixer',
        'libats',
        'libar-pal',
        'libar-acdb',
        'libar-gsl',
        'libar-gpr',
        'libar-pal',
        'libbatterylistener',
        'liblx-osal',
        'liblx-ar_util',
        'libfmpal',
        'lib_bt_aptx',
        'lib_bt_ble',
        'lib_bt_bundle',
        'libpalclient',
        'vendor.qti.hardware.pal@1.0-impl',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/bin/hw/android.hardware.security.keymint-service',
     'vendor/lib64/libskeymint_cli.so',
     'vendor/lib64/libskeymint10device.so',
     'vendor/lib64/vendor.samsung.hardware.keymint-V1-ndk_platform.so'): blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V4-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so'),

    'vendor/bin/hw/vendor.samsung.hardware.hyper-service': blob_fixup()
        .replace_needed('libhyper.so', 'libhyper_vendor.so'),
}

module = ExtractUtilsModule(
    'gts8wifi',
    'samsung',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'gts8wifi', module.vendor
    )
    utils.run()
