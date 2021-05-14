# rhsm-hide-facts

A tool to generate a custom fact override list for Red Hat Enterprise Linux systems, to help hide your confidential system information from RHSM.

This will blank out hostname and network information of your systems in the Red Hat Customer Portal. Currently it does not hide other information and I am assessing whether this can be done without any implications for RHEL licensing and auditing.

This tool is designed to be run directly on the system which needs to have its values protected. This is because the configuration of each system is different, so different facts will be exposed. For this reason it would be very difficult to expose a single unified "confidential.facts" file.

You can see an example `confidential.facts` override file in this directory as `confidential.facts.example`. You could take this file and adapt it to your own environment manually rather than using the script below, but it's unlikely to be a perfect fit for your systems.

## Usage

Make sure the system facts are up-to-date so the script can operate on all the relevant key/value pairs
```
sudo subscription-manager facts --update
```

Generate a confidential value mask based on your current system facts
This script needs to run with admin privileges to read the `/var/lib/rhsm/facts/facts.json` file.
```
sudo ./hidefacts.py
```

Check the confidential fact mask we've created
```
sudo cat /etc/rhsm/facts/confidential.facts
```

Update the facts on RHSM
```
sudo subscription-manager facts --update
```

Check your fact values by inspecting the systems on
https://access.redhat.com/management/systems/
