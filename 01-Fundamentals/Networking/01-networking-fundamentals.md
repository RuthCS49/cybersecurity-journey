# Networking Fundamentals
##### Date : september 11, 2026
##### Resource : Cisco Networking course
##### Level :Beginner

## What i learned today
Today i started learning about networking fundamentals as part of my cybersecurity studies  basics.Examples of the topics that i learned include :
   - Networking protocols and standards
   - OSI model and TCP/IP model
   - Networking Components
   - Network Media
   - Ethernet frames
   - How switches transfer data
The concepts helps us understand how devices communicate with each other.
## 1.Networking protocols and standards
Protocols are set of rules that govern how devices communicate across the network.They Include :
1. HTTP - Allows web browser to request and receive web pages , images or any other contents from a server.
2. FTP - Allows the transfer or sharing of files across the network.
3. UDP - Support connectionless and fast communication.
4. TCP - Ensures that data reach their destination correctly.
5. SMTP - Supports sending of email across the network.
6. DNS - It converts human-readable domain names to IP address for computers to understand.
7. DHCP - It  assigns IP addresses automatically on the network.

Protocols are essentials in cybersecurity because the explain how data moves across the systems. It allows professionals to detect threats or any anomalities,perform offensive security anf configure
defensive architetures.
Standards ensures that devices connecting to the network implement the same set of rules. Examples of standerd organizatios include: IEEE, IETF, TIA etc.
## 2.Networking Components
- End devies - They include computers , smartphone, cctv cameras
- Intermediate devices - They include routers, switches , access points
- Network media - They include fibre-optic cables, wireless transmission and wired cables
## 3.Network Media
Network media refers to the physical or wireless method used to carry network signals.They Include
- twisted-pair cable -Its an ethernet technology to connect devices
- Coaxial cable - It gives TV signals and makes up satellite communication systems
- Fibre-optic cables - carry information at very high speed over long distances( they are resistance to external electrical noise and interference
## 4.OSI model
1. Physical - Transmits raw bits over the physical medium
2. Data-link - defines the format of data on the network eg. adds frames
3. Network - decides which physical path the data will take
4. Transport - ensures data is transmitted to its destination( UDP & TCP)
5. Session - maintains connections and responsible for controlling ports and sessions
6. Presentation - ensures data is in a usable format and also supports data encryptions
7. Application - its a human- computer interaction layer to access network services
## 5.TCP/IP model
1. Network access layer(functions include those in physical and data-link layer in OSI model
2. internet layer
3. Transport layer(
4. Application layer ( functions include those in application, presentation and session layers of the OSI model)
## 6.Ethernet frames fields
Ethernet uses frames to transport data across the network. They include
- Preamble - it gets the NIC  card to recieving card in sync with the bytes that are coming down  the cable
- Start Frame Decimeter - indicates that the proceeding information is associated with the ethernet frame
- Destination MAC address
- Source MAC address
- Length/ type of information
- Data 
- Frame Check Sequence - ensures there are no errors during transmission
## 7. How switches transfer data 
switch uses MAC addresses to determine where Ethernet frames should be forwarded by building and using a MAC address table.
The processes include :
1. A frame arrives at a switch.
2. The switch examines the source MAC address and its not known its added in the MAC address table.
3. The switch can learn which port that source device is connected to.
4. The switch examines the destination MAC address.
5. If the destination MAC address is known, the switch forwards the frame through the appropriate port.
6. If the destination is unknown, the switch may flood the frame out the relevant ports except the port on which it arrived.
