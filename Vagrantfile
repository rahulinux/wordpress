# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "blacklabelops/centos6"
  config.vm.box_check_update = false
  config.vm.network "public_network" 
  config.vm.hostname = "wordpress.bigdecisions.loc"

  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = false
  
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end

  config.vm.provision 'ansible' do |ansible|
    ansible.verbose = 'vvv'
    ansible.playbook = 'provision/ansible/site.yml'
  end
end
