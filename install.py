#!/usr/bin/python

import os
os.system("sudo apt-get update ")
os.system("sudo apt-get install nginx -y")
os.system("sudo apt-get install apache2")
os.system("sudo apt-get install mysql-server php5-mysql -y")
os.system("sudo mysql_install_db")
# For complete install
os.system("sudo apt-get install php5 libapache2-mod-php5 php5-mcrypt -y") 


