#!usr/bin/python3
# pip install python-nmap
import nmap
scanner = nmap.PortScanner()
print("Welcome to simple nmap automation tool")
ip_addr = input("Enter the IP address to scan: ")

resp = input("""\nPlease enter the type of scan you want to run
             1)SYN ACK Scan
             2)UDP Scan
             3)Comprehensive Scan\n:""")

if resp == '1':
    print('Running SYN ACK Scan IP:',ip_addr)
    # for tcp
    scanner.scan(ip_addr,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print('IP status:',scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports:", scanner[ip_addr])
elif resp == '2':
    print('Running UDP Scan IP:',ip_addr)
    scanner.scan(ip_addr,'1-1024','-v -sU')
    print(scanner.scaninfo())
    # for UDP
    print('IP status:',scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports:", scanner[ip_addr])
elif resp == '3':
    print('Running Comprehensive Scan IP:',ip_addr)
    scanner.scan(ip_addr,'1-1024','-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print('IP status:',scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports:", scanner[ip_addr])
else:
    print('Please enter a valid option')
    exit()