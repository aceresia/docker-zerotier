#!/usr/bin/env python

import requests
import json
import os
import sys

if len(sys.argv) < 1:
    print "Usage: zerotier_allow.py <network id>"
    exit(-1)

NETWORK = sys.argv[1]

f = open("/var/lib/zerotier-one/identity.public", "r")
line = f.readline()
HOST_ID = line.split(":")[0]

headers = {
    'Connection': 'close',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer %s' % os.getenv("ZEROTIER_TOKEN")
}

r = requests.get('https://my.zerotier.com/api/network/%s/member/%s' % (
                                                                       NETWORK,
                                                                       HOST_ID
                                                                       ),
                 headers=headers)

data = r.json()

if data['config']['authorized'] != "true":
    data['config']['authorized'] = "true"

    r = requests.post('https://my.zerotier.com/api/network/%s/member/%s' % (
                                                                           NETWORK,
                                                                           HOST_ID
                                                                           ),
                      headers=headers, data=json.dumps(data))
