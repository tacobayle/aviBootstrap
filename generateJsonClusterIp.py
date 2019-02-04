import requests, json, os, yaml, sys
paramsFile = sys.argv[1]
password = sys.argv[2]
version = sys.argv[3]
username = 'admin'
with open(paramsFile, 'r') as stream:
    data_loaded = yaml.load(stream)
stream.close
clusterIP = data_loaded['avi']['controller']['clusterIp']
avi_credentials = { 'avi_credentials': {'controller' : clusterIP, 'username': username, 'password': password, 'api_version': version}}
# with open('vars/creds.yml', 'w') as outfile:
#     yaml.dump(avi_credentials, outfile, default_flow_style=False)
# outfile.close
print(json.dumps(avi_credentials))
