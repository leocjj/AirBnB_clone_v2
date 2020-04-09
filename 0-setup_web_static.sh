#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
ALIAS="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
SRC="/etc/nginx/sites-enabled/default"
sudo mkdir /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello World from:..." > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "30i $ALIAS" $SRC
sudo service nginx restart
