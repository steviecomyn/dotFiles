#!/bin/bash

# a Bash Script to select a server, enter username and password and connect to NordVPN.

# Selects a Random Server within Range of NordVPN UK Server list.
serverNumber=$(shuf -i 100-600 -n 1)

xfce4-terminal -e 'sh -c "sudo openvpn --config /etc/openvpn/ovpn_udp/uk$(shuf -i 100-600 -n 1).nordvpn.com.udp.ovpn --auth-user-pass /home/stevie/Scripts/vpn/pass.txt; exec bash"'
