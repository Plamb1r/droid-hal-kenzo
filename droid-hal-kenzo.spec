# These and other macros are documented in dhd/droid-hal-device.inc

%define device kenzo
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi Note 3 Pro

%define droid_target_aarch64 1

%define installable_zip 1

%define straggler_files \
/init.qcom.bt.sh\
/init.qcom.sh\
%{nil}

%include rpm/dhd/droid-hal-device.inc
