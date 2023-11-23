Ansible RabbitMQ role
=========

Here is Ansible example role of building and configuring RabbitMQ. 
Role includes Firewall config and creating test_exchange with test_queue and bind them together. 
Also includes python script for sending sample test messages to RabbitMQ queue.

Requirements
------------

This is created for Linux Debian 12, all reguired packages for instalation are added in install_nessesary_packages.yaml

Role Variables
--------------

In this role we have 2 users with encrypted passwods 'vault vault_test_user_password' and 'vault_admin_user_password' 
You can create your own users or use already created ones to connect to RabbitMQ management web:
test user pass: test
admin user pass: test123

Dependencies
------------

All tasks are split in diferent files for easier reading:
- import_tasks: install_nessesary_packages.yml
- import_tasks: install_repos.yml
- import_tasks: install_configure_rabbitmq.yml
- import_tasks: install_firewall.yml
- import_tasks: open_firewall.yml


Example Playbook
----------------

Including example of how to run ansible role:

Add this to  /etc/ansible/runsetup.yml:
```
---
- hosts: debian
  roles:
  - rabbitmq
```
Hit save and run with:
 /etc/ansible/runsetup.yml --ask-vault-pass

Vault pass is: test

License
-------

BSD

Author Information
------------------
General-RNG
