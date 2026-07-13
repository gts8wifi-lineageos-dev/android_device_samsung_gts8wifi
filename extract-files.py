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
    'device/samsung/gts8wifi',
    'vendor/samsung/gts8wifi',
    'hardware/samsung',
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
        'android.hardware.camera.provider@2.4-legacy',
        'android.hardware.camera.provider@2.5-legacy',
        'android.hardware.common-V2-ndk_platform',
        'android.hardware.gnss-V1-ndk_platform',
        'android.system.keystore2-V1-ndk_platform',
        'libagm',
        'libagmclient',
        'libagmmixer',
        'libats',
        'libar-pal',
        'libar-acdb',
        'libar-gsl',
        'libar-gpr',
        'libbatterylistener',
        'liblx-osal',
        'liblx-ar_util',
        'libfmpal',
        'lib_bt_aptx',
        'lib_bt_ble',
        'lib_bt_bundle',
        'libpalclient',
        'libagm_mixer_plugin',
        'libagm_compress_plugin',
        'libagm_pcm_plugin',
        'vendor.qti.hardware.pal@1.0-impl',
        'vendor.qti.hardware.AGMIPC@1.0-impl',
        'vendor.qti.hardware.AGMIPC@1.0',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib64/libqtikeymaster4.so',
     'vendor/lib64/libkeymasterutils.so',
     'vendor/lib64/libkeymasterdeviceutils.so',
     'vendor/lib64/libspcom.so',
     'vendor/bin/hw/android.hardware.keymaster@4.0-strongbox-service-qti'): blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-v33.so'),

     ('vendor/lib64/camx.device@3.2-impl.so',
      'vendor/lib64/camx.device@3.4-impl.so'): blob_fixup()
        .replace_needed('libcamera_provider_shim.so', 'libcamera_provider_shim.samsung.so')
        .add_needed('libcamera_provider_shim.samsung.so'),

    'vendor/lib64/vendor.samsung.hardware.camera.provider@4.0-legacy.so': blob_fixup()
        .replace_needed('libcamera_provider_shim.so', 'libcamera_provider_shim.samsung.so')
        .add_needed('libcamera_provider_shim.samsung.so')
        .replace_needed('camera.device@3.2-impl.so', 'camera.device@3.2-impl.samsung.so')
        .replace_needed('camera.device@3.3-impl.so', 'camera.device@3.3-impl.samsung.so')
        .replace_needed('camera.device@3.4-impl.so', 'camera.device@3.4-impl.samsung.so')
        .replace_needed('camera.device@3.5-impl.so', 'camera.device@3.5-impl.samsung.so'),

    'vendor/lib64/vendor.samsung.hardware.camera.device@5.0-impl.so': blob_fixup()
        .add_needed('libshim_camera.so')
        .replace_needed('camera.device@3.2-impl.so', 'camera.device@3.2-impl.samsung.so')
        .replace_needed('camera.device@3.3-impl.so', 'camera.device@3.3-impl.samsung.so')
        .replace_needed('camera.device@3.4-impl.so', 'camera.device@3.4-impl.samsung.so')
        .replace_needed('camera.device@3.5-impl.so', 'camera.device@3.5-impl.samsung.so'),

    ('vendor/lib/vendor.samsung.hardware.camera.provider@4.0-legacy.so',
     'vendor/lib/vendor.samsung.hardware.camera.device@5.0-impl.so'): blob_fixup()
        .replace_needed('camera.device@3.2-impl.so', 'camera.device@3.2-impl.samsung.so')
        .replace_needed('camera.device@3.3-impl.so', 'camera.device@3.3-impl.samsung.so')
        .replace_needed('camera.device@3.4-impl.so', 'camera.device@3.4-impl.samsung.so')
        .replace_needed('camera.device@3.5-impl.so', 'camera.device@3.5-impl.samsung.so'),

    ('vendor/lib64/libc2filterplugin.so',
     'vendor/lib64/unihal_android.so',
     'vendor/lib/libapex_cmn.so'): blob_fixup()
        .add_needed('libui_shim.so'),

    'vendor/etc/init/pa_daemon_qsee.rc': blob_fixup()
        .regex_replace('\n    start proca', ''),

    'vendor/etc/init/wifi_qcom.rc': blob_fixup()
        .regex_replace(r'service vendor\.cnss_dumpcollector .*\n(?:[ \t]+.*\n)*', '')
        .regex_replace(r'(?:stop|start) vendor\.cnss_dumpcollector\n', ''),

    'vendor/bin/hw/macloader': blob_fixup()
        .binary_regex_replace(b'vendor.wifi.dualconcurrent.interface', b'vendor.wiff.dualconcurrent.interface')
        .binary_regex_replace(b'ro.vendor.wifi.sap.interface', b'ru.vendor.wifi.sap.interface'),
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
