# aviBoostrap
## Prerequisites:
1. Make sure 1 or 3 Vm(s) has/have been deployed with the Avi software installed
2. Make sure avisdk is installed:
```
pip install avisdk==18.1.5b3
ansible-galaxy install -f avinetworks.avisdk
```

## Input:
An inventory file with the following format (could be 1 or 3 controller hosts):
```
all:
  children:
    controller:
      hosts:
        192.168.17.179:
```
## Use the ansible playbook to
1. Wait for the Avi portal to be up
2. Generate variable to feed the python SDK
3. Change the default password on the primary/first controller
4. Optionnally, configure the Azure cloud (for the cluster perspective)
5. Optionnally, configure the cluster without the IP cluster
6. Optionnally, configure the cluster with IP cluster (if controller hosts == 3 and avi.controller.clusterIp)
7. Check the status of the controller
8. Display a message with all the information
9. Configure SE group
10. Modify Avi controller Parameters (tenant)
11. Create a json file to feed next ansible playbook

## Parameters:
All the paramaters/variables are stored in var/params.yml:

## Run the playbook:
ansible-playbook -i hostsLocal main.yml

## Tests:
Playbooks have been tested against:
- Environment: Azure (wo cluster)
- Avi 17.2.14, 18.1.5
- Ansible 2.7.0

## Improvement:
Sometimes the playbook aviBootstrapCluster.yml fails at the first attempt (looks fixed):
```
TASK [Update user password] *********************************************************
fatal: [127.0.0.1]: FAILED! => {"changed": false, "module_stderr": "No handlers could be found for logger \"avi.sdk.avi_api\"\nTraceback (most recent call last):\n  File \"/home/avi/.ansible/tmp/ansible-tmp-1549270733.19-206298340575753/AnsiballZ_avi_useraccount.py\", line 113, in <module>\n    _ansiballz_main()\n  File \"/home/avi/.ansible/tmp/ansible-tmp-1549270733.19-206298340575753/AnsiballZ_avi_useraccount.py\", line 105, in _ansiballz_main\n    invoke_module(zipped_mod, temp_path, ANSIBALLZ_PARAMS)\n  File \"/home/avi/.ansible/tmp/ansible-tmp-1549270733.19-206298340575753/AnsiballZ_avi_useraccount.py\", line 48, in invoke_module\n    imp.load_module('__main__', mod, module, MOD_DESC)\n  File \"/tmp/ansible_avi_useraccount_payload_I22D54/__main__.py\", line 162, in <module>\n  File \"/tmp/ansible_avi_useraccount_payload_I22D54/__main__.py\", line 150, in main\n  File \"/home/avi/.local/lib/python2.7/site-packages/avi/sdk/avi_api.py\", line 417, in get_session\n    max_api_retries=max_api_retries)\n  File \"/home/avi/.local/lib/python2.7/site-packages/avi/sdk/avi_api.py\", line 274, in __init__\n    self.authenticate_session()\n  File \"/home/avi/.local/lib/python2.7/site-packages/avi/sdk/avi_api.py\", line 498, in authenticate_session\n    self.authenticate_session()\n  File \"/home/avi/.local/lib/python2.7/site-packages/avi/sdk/avi_api.py\", line 498, in authenticate_session\n    self.authenticate_session()\n  File \"/home/avi/.local/lib/python2.7/site-packages/avi/sdk/avi_api.py\", line 498, in authenticate_session\n    self.authenticate_session()\n  File \"/home/avi/.local/lib/python2.7/site-packages/avi/sdk/avi_api.py\", line 497, in authenticate_session\n    raise err\nrequests.exceptions.ConnectionError: HTTPSConnectionPool(host='172.16.1.40', port=443): Max retries exceeded with url: /login (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7fd36f12d050>: Failed to establish a new connection: [Errno 113] No route to host',))\n", "module_stdout": "", "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error", "rc": 1}
```
