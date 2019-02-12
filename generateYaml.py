import requests, json, os, yaml, sys
#
# This python script reads an ansible host inventory file like the following:
# ---
# all:
#   children:
#     jump:
#       hosts:
#         172.16.1.4:
#     controller:
#       hosts:
#         172.16.1.5:
#         172.16.1.6:
#         172.16.1.7:
#   vars:
#     ansible_user: "avi"
#     ansible_ssh_private_key_file: "/home/avi/.ssh/id_rsa.azure"
#
# and creates a yml file like the following:
#
# avi_cluster:
#   ip:
#   - 172.16.1.5
#   - 172.16.1.7
#   name: avi-cluster
# avi_credentials:
#   api_version: 17.2.14
#   controller: 172.16.1.6
#   password: Avi_2019
#   username: admin
#
hostFile = sys.argv[1]
password = sys.argv[2]
version = sys.argv[3]
username = 'admin'
with open(hostFile, 'r') as stream:
    data_loaded = yaml.load(stream)
stream.close
try:
  controllerLeader = [*data_loaded['all']['children']['controller']['hosts']][0]
except:
  exit()
if len([*data_loaded['all']['children']['controller']['hosts']]) == 1:
  avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version}, 'avi_cluster': False}
if len([*data_loaded['all']['children']['controller']['hosts']]) == 3:
  controllerFollower = []
  controllerFollower.append([*data_loaded['all']['children']['controller']['hosts']][1])
  controllerFollower.append([*data_loaded['all']['children']['controller']['hosts']][2])
  avi_credentials = { 'avi_credentials': {'controller' : controllerLeader, 'username': username, 'password': password, 'api_version': version}, 'avi_cluster': {'name': 'avi-cluster', 'ip': controllerFollower }}
with open('vars/creds.yml', 'w') as outfile:
    yaml.dump(avi_credentials, outfile, default_flow_style=False)
outfile.close
