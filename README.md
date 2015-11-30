# WordPress Automation

If you want to setup wordpress in your VM for testing purpose, then this repository useful for you. it will install CentOS6 Minimal with MySQLServer, PHP, Apache and Wordpress. If you want to modify settings like username, password, path, urls you can edit the global varible file located at `provision/ansible/group_vars/all`

### Prerequisite
I am assuming following things are already installed on your Laptop or Desktop
  - [VirtualBox] : ( Version 4.3.x or higher ) 
  - [Vagrant]: ( 1.7.4 or higher )
  - [Ansible]: ( 1.9.4 or higher )
  - [Git client] 

[VirtualBox]: <https://en.wikipedia.org/wiki/VirtualBox>
[Vagrant]:<https://en.wikipedia.org/wiki/Vagrant_%28software%29>
[Ansible]:<https://en.wikipedia.org/wiki/Ansible_%28software%29>
[Git client]: <https://en.wikipedia.org/wiki/Git_%28software%29>

Download the WordPress Repository 
```sh
git clone https://github.com/rahulinux/wordpress
```

Setup WordPress
```sh
cd wordpress
vagrant up
```

After finishing the VM setup it will print the IPAddress, please note this IPAddress

in case if you unable to see the IPAddress you can get that using below command:

```sh
vagrant ssh -c "ifconfig eth1 | grep -o -P '(?<=inet addr:)[0-9\.]*(?=)'"
```

Once your VM is ready you can access the blog, but since it's VM you need to map VM IPAddress to the hostname as below

```sh
IP=$( vagrant ssh -c "ifconfig eth1 | grep -o -P '(?<=inet addr:)[0-9\.]*(?=)'" )
sudo bash -c "echo $IP wordpress.bigdecisions.loc >> /etc/hosts" 
```
Now you can browse your blog at http://wordpress.bigdecisions.loc 
Default Username: admin and Password: admin
