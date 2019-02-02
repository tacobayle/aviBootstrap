# aviBoostrap
## Prerequisites:
Make sure 1/3 Vm(s) has/have been deployed with the Avi software installed

## Input:
An inventory file with the following format (could be 1 or 3 controller hosts):
'---
all:
  children:
    controller:
      hosts:
        192.168.17.179:'

## Use the ansible playbook to
- Generate a yaml file with all the information (to feed the python SDK)
- Wait for the Avi portal to be up
- Change the default password on the primary/first controller
- Configure the Azure cloud (if avi.controller.cloud == azure and controller hosts == 3 and avi.controller.clusterIp)
- Configure the cluster without the IP cluster (if controller hosts == 3 and not avi.controller.clusterIp)
- Configure the cluster with IP cluster (if controller hosts == 3 and avi.controller.clusterIp)
- Check the status of the controller
- Display a message with all the information

All the paramaters are stored in var/params.yml

avi:
  controller:
    newPassword: XXXXXX
    version: 17.2.14
    clusterIpStatus: true
    clusterIp: 172.16.1.10
    cloud: azure

Example:
ansible-playbook -i hosts main.yml

All the variables are stored in vars/params.yml

Playbooks have been tested against:
- Env: Ubuntu 16.04, Azure
- Avi 17.2.14
- Ansible 2.7.0
