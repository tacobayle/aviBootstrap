# aviBoostrap
## Prerequisites:
1. Make sure 1 or 3 Vm(s) has/have been deployed with the Avi software installed


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
1. Generate a yaml file with all the information (to feed the python SDK)
2. Wait for the Avi portal to be up
3. Change the default password on the primary/first controller
4. Configure the Azure cloud (if avi.controller.cloud == azure and controller hosts == 3 and avi.controller.clusterIp)
5. Configure the cluster without the IP cluster (if controller hosts == 3 and not avi.controller.clusterIp)
6. Configure the cluster with IP cluster (if controller hosts == 3 and avi.controller.clusterIp)
7. Check the status of the controller
8. Display a message with all the information

## Parameters:
All the paramaters/variables are stored in var/params.yml:
```
avi:
  controller:
    newPassword: XXXXXX
    version: 17.2.14
    clusterIpStatus: true
    clusterIp: 172.16.1.10
    cloud: azure
```

## Run the playbook:
ansible-playbook -i hosts main.yml

## Tests:
Playbooks have been tested against:
- Environment: Ubuntu 16.04, Azure and GCP
- Avi 17.2.14, 18.1.5
- Ansible 2.7.0
