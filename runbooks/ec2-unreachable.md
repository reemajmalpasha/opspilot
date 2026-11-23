# EC2 instance running but the application is not reachable
Check from outside in: instance, network, operating system, application.
1. Instance: state is running and status checks show 2/2 passed.
2. Network: the security group allows the application port from your IP, the NACL allows inbound and outbound traffic, the route table sends 0.0.0.0/0 to the Internet Gateway, and the instance has a public or Elastic IP.
3. Operating system: ufw or iptables is not blocking the port.
4. Application: the service is running and listening on the right port on 0.0.0.0, not only 127.0.0.1. Use ss -tulnp and systemctl status, then read the application logs.
5. If SSH is not possible, use EC2 Instance Connect or SSM Session Manager.
