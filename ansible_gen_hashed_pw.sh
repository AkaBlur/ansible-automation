#!/bin/bash

SALT=$(dd status=none count=12 bs=1 if=/dev/urandom | base64 | tr [=/+] 0)

echo "Enter password to hash:"
read -s PASSWORD_ENTER
echo "Retype password:"
read -s PASSWORD_REENTER

if [ "${PASSWORD_ENTER}" != "${PASSWORD_REENTER}" ]; then
    echo "Password don't match!"
    exit 1
else
    ansible all -i localhost, -m debug -a "msg={{ '${PASSWORD_REENTER}' | password_hash('sha512', '${SALT%=}') }}"
    exit 0
fi
