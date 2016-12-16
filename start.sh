#!/bin/bash

set -e

/sbin/MAKEDEV tun
sleep 1
/usr/sbin/zerotier-one -d

sleep 5
/usr/sbin/zerotier-cli join $NETWORK

sleep 10

python /zerotier_allow.py $NETWORK

if [ -n "$MTU" ]; then
  ip link set zt0 mtu $MTU
fi

while [ 1 ]; do
  ip addr
  sleep 30
done
