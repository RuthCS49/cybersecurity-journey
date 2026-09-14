# LINUX networking 
I learnt how to inspect network configuration on Ubuntu and understand how IP addressing, routing, ICMP, and ARP work together during network communication.
## 1.Viewing networking interface
I used the following command to view the network interfaces on my Ubuntu system:

ip addr-The command displayed three interfaces:
- lo — loopback interface
- enp0s31f6 — Ethernet interface
- wlp0s20f3 — Wi-Fi interface
##### Ethernet configuration
My active Ethernet interface was:
- Interface: enp0s31f6
- IPv4 address: 192.168.0.101/24
- MAC address: 64:1c:67:ba:9c:41
- State: UP

The /24 prefix corresponds to the subnet mask: 255.255.255.0
This places the computer on the: 192.168.0.0/24 network.
The Ethernet interface received its IPv4 configuration dynamically through DHCP.
##### Wi-Fi
The Wi-Fi interface was:
wlp0s20f3
It was in the DOWN state because the computer was currently using the Ethernet connection.
## 2.Viewing the Routing Table
I used: ip route.

The routing table showed: default via 192.168.0.1 dev enp0s31f6 proto dhcp src 192.168.0.101 metric 100.
Interpretation

The first route:

default via 192.168.0.1 means that 192.168.0.1 is the default gateway.

The second route:

192.168.0.0/24 dev enp0s31f6 means that the 192.168.0.0/24 network is directly connected through the Ethernet interface.

Therefore:
- Computer: 192.168.0.101
- Network: 192.168.0.0/24 
- Default gateway: 192.168.0.1
- Interface: enp0s31f6
## 3.Testing Connectivity with ICMP
I used the ping command to test connectivity.

Test 1: Default gateway

Command: ping -c 4 192.168.0.1

Result: 4 packets transmitted, 4 received, 0% packet loss and Average round-trip time: 0.512 ms

Interpretation

The test confirmed that my computer could successfully communicate with its default gateway over the local network.

Test 2: External IP address

Command: ping -c 4 8.8.8.8
Result:

4 packets transmitted, 4 received, 0% packet loss and Average round-trip time: 287.237 ms

Interpretation

The successful replies showed that my computer could reach an external IP address through the default gateway and the Internet.

Test 3: Domain name
Command: ping -c 4 google.com

The hostname resolved to: 172.217.170.206

Result:

4 packets transmitted, 4 received, 0% packet loss

Interpretation

This demonstrated that hostname resolution was working and that the computer could communicate with the resolved destination.
## 4.What is ICMP?
ICMP stands for Internet Control Message Protocol.

It is used for network diagnostics, error reporting, and control information.

The ping command uses ICMP Echo Requests and Echo Replies to test whether a destination is reachable.

The time reported by ping represents the approximate round-trip time for the request and reply.
## 5. What is ARP?
ARP stands for Address Resolution Protocol.

For IPv4 networks, ARP is used to determine the MAC address associated with an IPv4 address on the local network.

For example, if my computer needs to communicate with: 192.168.0.1

it needs to determine the router's MAC address so that it can construct an Ethernet frame for local delivery.

Conceptually: ARP therefore connects Layer 3 IPv4 addressing with Layer 2 Ethernet addressing.

#### ARP observation 
I used ip neigh and that ouput was 192.168.0.1 dev enp0s31f6 lladdr b4:0f:3b:0b:ef:a0 REACHABLE 

This showed that my computer had an IPv4-to-MAC mapping for the default gateway: 192.168.0.1 → b4:0f:3b:0b:ef:a0

The dev enp0s31f6 portion indicates that the mapping is associated with my Ethernet interface.

REACHABLE indicates that Linux currently considers the neighbour reachable.

This demonstrates how ARP allows an IPv4 address on the local network to be associated with a MAC address for Ethernet communication.

## 6. How ICMP and ARP Work Together
When I ping a device on the local network, several networking concepts work together.

For example:
ping -c 4 192.168.0.1
Conceptually:
1. Computer wants to reach 192.168.0.1
2. ARP determines the destination MAC address
3. Computer creates an Ethernet frame
4. Ethernet frame carries an IP packet
5. IP packet carries an ICMP Echo Request
6. Router sends an ICMP Echo Reply
This demonstrates the relationship between:  MAC addresses ,Ethernet, IP and ICMP
## 7. Cybersecurity Relevance
Understanding these protocols is important for cybersecurity because network defenders need to understand how legitimate network communication works before they can recognize abnormal behavior.
Important concepts include:
- IP addressing
- MAC addresses
- ARP
- Ethernet frames
- Routing
- ICMP
- DNS
- Network interfaces
- Default gateways
ARP is particularly relevant to network security because attackers can attempt to manipulate ARP information. This makes understanding normal ARP behavior important for detecting suspicious network activity.
## 8. What I Learned
From this exercise, I learned how to:
1. Inspect network interfaces using ip addr.
2. Identify an IPv4 address and subnet prefix.
3. Identify a MAC address.
4. Identify the active network interface.
5. Inspect the routing table using ip route.
6. Identify the default gateway.
7. Understand the purpose of ICMP.
8. Understand how ping uses ICMP.
9. Understand the purpose of ARP.
10. Understand the relationship between IP addresses and MAC addresses.
11. Connect Layer 2 and Layer 3 networking concepts.

