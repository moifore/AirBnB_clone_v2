#!/usr/bin/env bash
# Script sets up my web servers 117692-web-01 and 117692-web-02 for deployment of web_static
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
    echo "Nginx is not installed. Installing now..."
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create web server directory structure
sudo mkdir -p /data/web_static/{releases,test,shared}

# Create fake HTML file for testing Nginx configuration
echo "<html><body>Hello World!</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link to test release
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership and permissions for web server directory
sudo chown -R ubuntu:ubuntu /data/
sudo chmod -R 755 /data/

# Configure Nginx to serve content from web_static directory
sudo sed -i '/server_name _;/a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart

