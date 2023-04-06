#!/usr/bin/env bash

# Install Nginx if it's not already installed
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get install nginx -y
fi

# Create the necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file for testing purposes
echo "ALX School" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link from /data/web_static/current to /data/web_static/releases/test
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Update Nginx configuration to serve content from /data/web_static/current to /hbnb_static
sudo sed -i '/^}/i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart

