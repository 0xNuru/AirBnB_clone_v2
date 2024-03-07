#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update > /dev/null
sudo apt-get install -y nginx > /dev/null


sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "testing nginx 123" | sudo tee /data/web_static/releases/test/index.html

if [ -d "/data/web_static/current" ]
then
        sudo rm -rf /data/web_static/current
fi

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

# Configure nginx to serve content pointed to by symlink to hbnb_static using alias
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart server
sudo service nginx restart
