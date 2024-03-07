#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

apt-get -y update > /dev/null
apt-get install -y nginx > /dev/null


mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "testing nginx 123" > /data/web_static/releases/test/index.html

if [ -d "/data/web_static/current" ]
then
        sudo rm -rf /data/web_static/current
fi

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Configure nginx to serve content pointed to by symlink to hbnb_static using alias
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart server
service nginx restart
