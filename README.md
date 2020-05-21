# RIP-ANSIBLE
RIP-ANSIBLE with Firewall
This playbook does the following:

The Python script performs the following configuration operations:

1. Configures the interfaces according to the table below (including the loopback interface):
Interface    connected physical interface   loopback interface
Router A     42.7.1.1/24                     42.7.10.1/24
Router B     42.7.1.2/24                     42.7.20.1/24

 
2. Configures RIP routing protocol on the connected interfaces. 
3. Configures the stateful firewall to let through pings and RIP routing protocol updates.

4. Configure a stateless input firewall filter on the connected
physical interface of one of the routers that 

    a) allows management access only from the IP address of the connected router’s
    remote interface; 
    b) denies management access from any other IP addresses and counts the attempts to do so; 
    c) allows any non-management traffic from anywhere and counts the nonmanagement packets. 

  5. Check's the routers routing tables and make sure that the network configured on the remote router’s loopback interface shows up in the local router’s routing table.

 6. Ping's the remote loopback interface from the local router and verify that the loopback interface is reachable. 

 7. Check's the firewall counter values and verify that they are incremented correctly.

*To run the playbooks run:*
ansible-playbook all_playbook.yaml


This invokes the
rip_playbook.yaml and confcheck_playbook.yaml


NOTE: You need to change the inventory file to include your Routers IP and interface address. The txt files are created after running the playbooks and will be different for you.
