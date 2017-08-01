#!/bin/bash

cp ./pishutter.py /usr/bin

echo "[Unit]
Description=Control ir cut filter based on sunrise and sunset
After=network.target
[Service]
Type=simple
ExecStart=/usr/bin/python2 /usr/bin/pishutter.py
Restart=on-failure
[Install]
WantedBy=multi-user.target">/lib/systemd/system/pishutter.service

systemctl enable pishutter
