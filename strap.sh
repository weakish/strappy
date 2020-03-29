#!/bin/sh

# Assuming the os is debian/ubuntu.
# Run this as root.

set -e

# update system
apt update
apt upgrade --assume-yes --quite

# python3.8
apt install --assume-yes --quite python3.8
update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2

# essential tools
apt install --assume-yes --quite git curl aptitude