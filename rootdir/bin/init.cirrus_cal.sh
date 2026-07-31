#! /vendor/bin/sh

# Copyright (C) 2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0

# Load the factory speaker calibration into the Cirrus CS35L45 amps.

EFS_DIR=/efs/cirrus
CAL_DIR=/sys/class/cirrus/cirrus_cal

POLL_INTERVAL=0.05
MAX_TRIES=600 # 30s

log()
{
	echo "init.cirrus_cal: $*" > /dev/kmsg
}

queue()
{
	val=$(cat "$EFS_DIR/$1" 2>/dev/null)

	case $val in
	"" | *[!0-9]* | 0)
		return 0
		;;
	esac

	worklist="$worklist $2=$val"
}

worklist=""

queue temp_cal temp

# cirrus,mfd-suffix: "" rear-left, _b front-left, _r rear-right, _br front-right
for suffix in "" _b _r _br
do
	queue "rdc_cal$suffix" "rdc$suffix"
done

if [ -z "$worklist" ]
then
	log "no usable EFS calibration, leaving driver defaults in place"
	exit 0
fi

pending=$worklist
tries=0

while [ "$tries" -lt "$MAX_TRIES" ]
do
	remaining=""

	for item in $pending
	do
		node=${item%%=*}
		val=${item#*=}

		if [ -w "$CAL_DIR/$node" ]
		then
			echo "$val" > "$CAL_DIR/$node"
		fi

		if [ "$(cat "$CAL_DIR/$node" 2>/dev/null)" != "$val" ]
		then
			remaining="$remaining $item"
		fi
	done

	pending=$remaining

	if [ -z "$pending" ]
	then
		break
	fi

	sleep $POLL_INTERVAL
	tries=$((tries + 1))
done

if [ -n "$pending" ]
then
	log "gave up after $tries tries, unconfirmed:$pending"
else
	log "applied EFS calibration after $tries tries:$worklist"
fi

exit 0
