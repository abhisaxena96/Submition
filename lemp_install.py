#!/bin/bash/python
from os import system
import time
print("STARTING LEMP::")
system("cd ~")
system("sudo apt-get update")
system("sudo apt-get install nginx")
system("sudo ufw allow 'Nginx HTTP'")
system("sudo ufw status")
system("ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'")
print("To chech whether ip is working or not\n run command : curl -4 icanhazip.com\n on new terminal")
time.sleep(1000)
print("security script for mysql starting....!!")

system("sudo mysql_secure_installation")

print("\nstarting php....::")
system("sudo apt-get install php-fpm php-mysql")

print("\nconfigure php processor.......!!\nchange in file : cgi.fix_pathinfo=0")
time.sleep(100)
system("sudo nano /etc/php/7.0/fpm/php.ini")
system("sudo systemctl restart php7.0-fpm")

print("""server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index ((index.php)) index.html index.htm index.nginx-debian.html;

    server_name ((server_domain_or_IP;))

    ((location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.0-fpm.sock;
    }

    location ~ /\.ht {
        deny all;
    }))
}""")
print("changes need to make in the file   ::::")
time.sleep(3000)
system("sudo nano /etc/nginx/sites-available/default")

print("ENDING ....::")

