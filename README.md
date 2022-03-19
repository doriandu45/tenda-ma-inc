# Automatic MAC address increase for Tenda AC10

## What?

This script is intended to automatically increase your spoofed MAC address on a Tenda AC10 router. **Please not that it may not work on another models, it depends of the firmware**

## Why?

Quantic Telecom (our student housing ISP) enforce a policy that prevent the use of a NAT in our local network (they want us to login on each device every 2 weeks) by banning the MAC address on each 15-day reset. Since I want to still use my NAT (mainly so I don't have to log back in on ALL of my devices), and I am tired to change my spoofed MAC everytime, I made this little script and coupled it with [this auto-login script](https://github.com/Lymkwi/quantelconnect)

## How?

Simply put your password on the `creds.json` file (**keep the `username=admin` even if your router don't have an username system**) and simply call the script

## WARNING

I am not responsible for what you do with my script. Also, please note that the error-handling is inexistant, since I don't really need it and this script is for a very specific use-case for a very specific device.
