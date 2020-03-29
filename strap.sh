#!/bin/sh

# Assuming the os is debian/ubuntu.
# Run this as root.

set -e

# update system
apt update
apt upgrade -y -q

# python3.8
apt install python3.8 -y -q
update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2

# essential tools
apt install git curl aptitude -y -q