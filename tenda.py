#!/usr/bin/python3
import requests
import json
import hashlib

AUTH_URL='http://192.168.0.1/login/Auth'
MAC_URL_GET='http://192.168.0.1/goform/AdvGetMacMtuWan'
MAC_URL_SET='http://192.168.0.1/goform/AdvSetMacMtuWan'

with open("creds.json", 'r') as f:
	data=json.load(f)

# Encodes the password in MD5 since that's what the router needs
data['password']=(hashlib.md5(bytes(data['password'],'utf8'))).hexdigest()

i = 0
while True:
	# Authentication
	r = requests.post(AUTH_URL, data)
	# Keep the session cookies
	c = r.history[0].cookies

	r = requests.get(MAC_URL_GET, cookies=c)

	# For obscure reason, sometimes we get redirected to the login page, and we need to log in a second time
	if len(r.history) == 0:
		break
	# To avoid infinite loop
	i = i + 1
	if i > 5:
		print("Authentication error?")
		exit()
	

current_mac=r.json()['wanInfo'][0]['mac']
current_mac = current_mac.split(':')
# Increment the last digit
current_mac[5]=str(hex(int(current_mac[5],16)+1))[2:]
if len(current_mac[5]) == 1:
	current_mac[5]="0"+current_mac[5]
current_mac=':'.join(current_mac)

# Forge the new request
data = { 'wanMTU': r.json()['wanInfo'][0]['wanMTU'], 'wanSpeed': r.json()['wanInfo'][0]['wanSpeed'], 'cloneType': r.json()['wanInfo'][0]['cloneType'], 'mac': current_mac }

requests.post(MAC_URL_SET, cookies=c, data=data)
print("Successfully set the MAC address to " + current_mac)