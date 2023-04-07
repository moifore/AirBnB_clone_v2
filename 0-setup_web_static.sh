#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

# Define color variables
GREEN='\033[1;32m'
NC='\033[0m' # No Color

# Update packages and install nginx
sudo apt-get update -y
sudo apt-get install -y nginx

# Configure firewall to allow incoming HTTP connections
sudo ufw allow 'Nginx HTTP'

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create test HTML file with welcome message
echo "<h1>Holberton School</h1>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Remove existing symlink if it exists
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi

# Create symbolic link to latest version of web_static
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/web_static/

# Add Nginx configuration for serving static files
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Enable Nginx configuration
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Restart nginx to apply changes
sudo service nginx restart

# Print success message
echo -e "${GREEN}Web server setup complete!${NC}"

