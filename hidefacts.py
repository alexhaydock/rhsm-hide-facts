#!/usr/bin/env python3

#
# hidefacts.py (v1.0 - 2021-05-14)
# ---
#
# A script to mask certain system facts from being
# reported back to Red Hat via RHSM.
#
# Alex Haydock
# alex@alexhaydock.co.uk
#

import re
import json

# Read our facts.json file
with open('/var/lib/rhsm/facts/facts.json') as json_file:
    facts = json.load(json_file)

# Isolate out the net.* facts, as these are the main ones we want to
# mask from being published.
network_facts = {k:facts[k] for k in facts if re.match('^net.*|^network.*', k)}

# Mask the network facts by replacing every value with 'confidential'
masked_facts = {x: 'confidential' for x in network_facts}

# Mask some other typically-confidential facts
masked_facts["uname.nodename"] = "confidential"

# Write out to confidential.facts
with open('/etc/rhsm/facts/confidential.facts', 'w') as outfile:
    json.dump(masked_facts, outfile)
