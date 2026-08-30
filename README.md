# CmdFleet
A command-line interface tool to help system administrators run a command across multiple servers with just a simple command.

## Installation Guide
to install CmdFleet you first need to clone this repository
```git clone https://github.com/snitchbossdotcom/cmdfleet/```

then you will cd into the directory
```cd cmdfleet```

now finally you will install all the required packages
```pip3 install -r requirements.txt```

## How To Use
To use it first you have to add your device's public ssh key to all of your servers

Then add all your servers ips to ips.txt

### Example
root@192.168.100.64
user@10.10.10.43
wah@185.165.29.94 -p 2022
root@192.168.164.83 -p 8373

after that you can run ```python3 app.py -c "command"```
### Example
<img width="467" height="226" alt="image" src="https://github.com/user-attachments/assets/694d8fdd-ef49-4598-9766-88f8ddc0351e" />



