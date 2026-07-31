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
        'lib_android_keymaster_keymint_utils',
        'libkeymaster4_1support',
        'libkeymaster4support',
        'libkeymaster_messages',
        'libkeymaster_portable',
        'libkeymint',
        'libpuresoftkeymasterdevice',
        'libsoft_attestation_cert',
    ): lib_fixup_vendor_suffix,
    (
        'android.hardware.camera.provider@2.4-legacy',
        'android.hardware.camera.provider@2.5-legacy',
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
    ('vendor/lib64/libsnapdragoncolor-manager.so',): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2_1.so'),

    ('vendor/bin/hw/android.hardware.gnss-aidl-service-qti',
     'vendor/lib/hw/android.hardware.gnss-aidl-impl-qti.so',
     'vendor/lib64/hw/android.hardware.gnss-aidl-impl-qti.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),

    ('vendor/lib/vendor.qti.hardware.display.config-V1-ndk_platform.so',
     'vendor/lib/vendor.qti.hardware.display.config-V2-ndk_platform.so',
     'vendor/lib/vendor.qti.hardware.display.config-V3-ndk_platform.so',
     'vendor/lib/vendor.qti.hardware.display.config-V4-ndk_platform.so',
     'vendor/lib/vendor.qti.hardware.display.config-V5-ndk_platform.so',
     'vendor/lib/vendor.qti.hardware.display.config-V6-ndk_platform.so',
     'vendor/lib64/vendor.qti.hardware.display.config-V1-ndk_platform.so',
     'vendor/lib64/vendor.qti.hardware.display.config-V2-ndk_platform.so',
     'vendor/lib64/vendor.qti.hardware.display.config-V3-ndk_platform.so',
     'vendor/lib64/vendor.qti.hardware.display.config-V4-ndk_platform.so',
     'vendor/lib64/vendor.qti.hardware.display.config-V5-ndk_platform.so',
     'vendor/lib64/vendor.qti.hardware.display.config-V6-ndk_platform.so',
     'vendor/lib64/vendor.samsung.hardware.media.mpp-V5-ndk_platform.so'): blob_fixup()
        .replace_needed('android.hardware.common-V2-ndk_platform.so', 'android.hardware.common-V2-ndk.so'),

    ('vendor/lib64/libqtikeymaster4.so',
     'vendor/lib64/libkeymasterutils.so',
     'vendor/lib64/libkeymasterdeviceutils.so',
     'vendor/lib64/libspcom.so',
     'vendor/bin/hw/android.hardware.keymaster@4.0-strongbox-service-qti'): blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-v33.so'),

    ('vendor/bin/hw/android.hardware.security.keymint-service_samsung',
     'vendor/lib64/libskeymint_cli.so',
     'vendor/lib64/libskeymint10device.so',
     'vendor/lib64/vendor.samsung.hardware.keymint-V1-ndk_platform.so'): blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V1-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
        .add_needed('android.hardware.security.rkp-V3-ndk.so')
        .replace_needed('libcrypto.so', 'libcrypto-v33.so')
        .replace_needed('libcppbor_external.so', 'libcppbor.so')
        .add_needed('libbase_compat_shim.so')
        .replace_needed('libkeymaster_portable.so', 'libkeymaster_portable_samsung.so')
        .replace_needed('libkeymint.so', 'libkeymint_samsung.so')
        .replace_needed('libpuresoftkeymasterdevice.so', 'libpuresoftkeymasterdevice_samsung.so')
        .replace_needed('libkeymaster4support.so', 'libkeymaster4support_samsung.so')
        .replace_needed('libkeymaster4_1support.so', 'libkeymaster4_1support_samsung.so'),

    ('vendor/lib64/libkeymint_samsung.so',
     'vendor/lib64/lib_android_keymaster_keymint_utils_samsung.so',
     'vendor/lib64/libkeymaster_portable_samsung.so',
     'vendor/lib64/libpuresoftkeymasterdevice_samsung.so',
     'vendor/lib64/libkeymaster4support_samsung.so',
     'vendor/lib64/libkeymaster4_1support_samsung.so',
     'vendor/lib64/libkeymaster_messages_samsung.so',
     'vendor/lib64/libsoft_attestation_cert_samsung.so'): blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V1-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
        .replace_needed('libcrypto.so', 'libcrypto-v33.so')
        .replace_needed('libcppbor_external.so', 'libcppbor.so')
        .replace_needed('lib_android_keymaster_keymint_utils.so', 'lib_android_keymaster_keymint_utils_samsung.so')
        .replace_needed('libkeymaster_messages.so', 'libkeymaster_messages_samsung.so')
        .replace_needed('libkeymaster_portable.so', 'libkeymaster_portable_samsung.so')
        .replace_needed('libpuresoftkeymasterdevice.so', 'libpuresoftkeymasterdevice_samsung.so')
        .replace_needed('libsoft_attestation_cert.so', 'libsoft_attestation_cert_samsung.so')
        .replace_needed('libkeymaster4support.so', 'libkeymaster4support_samsung.so'),

    'vendor/etc/init/android.hardware.security.keymint-service.rc': blob_fixup()
        .regex_replace(
            '/vendor/bin/hw/android.hardware.security.keymint-service\n',
            '/vendor/bin/hw/android.hardware.security.keymint-service_samsung\n',
        ),

    'vendor/lib64/hw/gatekeeper.mdfpp.so': blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-v33.so'),

    ('vendor/lib64/libc2filterplugin.so',
     'vendor/lib64/unihal_android.so',
     'vendor/lib/libapex_cmn.so'): blob_fixup()
        .add_needed('libui_shim.so'),

    'vendor/etc/init/pa_daemon_qsee.rc': blob_fixup()
        .regex_replace('\n    start proca', ''),

    'vendor/etc/init/vendor.qti.media.c2audio@1.0-service.rc': blob_fixup()
        .regex_replace(
            r'(service vendor-qti-media-c2audio-hal-1-0 [^\n]*\n)(?!    interface )',
            r'\1    interface android.hardware.media.c2@1.0::IComponentStore default2\n',
        ),

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
