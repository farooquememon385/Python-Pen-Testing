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
    print()
    scanner.scan(ip_addr,'1-1024','-v -sS')
    print(scanner.scaninfo())