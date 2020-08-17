#!/usr/bin/env bash
# script that sets up your web servers for the deployment
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "holberton index" > /data/web_static/releases/test/index.html
sudo touch /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
