""" Port Scanner Tool  

        Author: Abdelrhman Ahmed Abdelmonem
        Department: Software Engineer
        Date of Publish: 12/3/2025
        LinkedIn: https://www.linkedin.com/in/%D9%90abdelrhman-ahmed-82609b296/
        
"""




import socket, os, time, sys

class Menu:
    
    def displayMenu(self):
        
            print( "\n","\033[36m ██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗\n", 
                        " ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗\n",
                        " ██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝\n",
                        " ██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗\n",
                        " ██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║\n",
                        " ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝\033[0m")
            
    
    def displayOptions(self):

            print(      "\033[31m  ==========================[\033[34m PORT SCANNER TOOL FOR CYBER SECURITY USAGE \033[31m]==========================\n\033[0m")
            print("\033[32m  [DESCRIPTION]\033[0m")
            print("\t  This manual page documents port scanner tool. For only cyber security use.\n")
            print("\033[32m  [USAGE]\033[0m")
            print("\t  --help/-h\t\t\t\tFor display commands/options.\n")   
            print("\t  pscan [IP ADDRESS] [P1]-[P2]\t\tScan range of ports from P1 to P2 on a given ip address.\n") 
            print("\t  pscan [IP ADDRESS] [P]\t\tScan port P on a given ip address.\n") 
            print("\t  --exit/-e\t\t\t\tFor exit the tool.\n")   
            
    def getCommand(self):
        
            command = input("<PS> ")
            if command == "":
                return self.getCommand()  
            
            keys = command.split()
            # print(len(keys))    
            
            if keys[0] == "--help" or keys[0] == "-h":
                self.displayOptions()
                return self.getCommand()
            
            elif keys[0] == "pscan" and len(keys) > 2 and len(keys) < 4 and "-" not in keys[2]:
                
                newThread = Thread(keys[1], keys[2], 0)
                
                if not newThread.ipCheck():
                    print("Error: Invalid IP Address")
                    return self.getCommand() 
                if not newThread.portCheck():
                    print("Error: Invalid Port Number")
                    return self.getCommand() 
                
                print(newThread.startProcess())
                del newThread
                return self.getCommand()
                
            
            elif keys[0] == "pscan" and len(keys) > 2 and len(keys) < 4 and "-" in keys[2]:
                
                ports = keys[2].split("-")
                newThread = Thread(keys[1], ports[0], ports[1])  
                
                if not newThread.ipCheck():
                    print("Error: Invalid IP Address")
                    del newThread
                    return self.getCommand() 
                if not newThread.portCheck():
                    print("Error: Invalid Port Number")
                    del newThread
                    return self.getCommand() 
                
                print(newThread.startProcess())
                del newThread
                return self.getCommand()  
            
            elif keys[0] == "--exit" or keys[0] == "-e":
                count = 3
                while count > 0:
                    sys.stdout.write(f"Exiting tool in {count} seconds...\n")
                    time.sleep(1)
                    sys.stdout.write("\033[F\033[K")
                    sys.stdout.flush()
                    count -= 1
                os.system("cls")
                    
            else:
                print("Error: command not found")
                return self.getCommand()    

class Thread:
    
    def __init__(self, ip, port1, port2 = 0):
        self.ip = ip
        self.port1 = port1
        self.port2 = port2
        
    def ipCheck(self):
        ip = str(self.ip)
        ipDigits = ip.split(".")
        try:
            if len(ipDigits) == 4:
                for x in range(4):
                    if int(ipDigits[x]) < 0 or int(ipDigits[x]) > 255:
                        return False
                return True  
        except:
            return False        
    
    def portCheck(self):
        if self.port2 == 0:
            try:
                port = str(self.port1)
                if int(port) > 65355 or int(port) < 1:
                    return False
                return True
            except:
                return False
        else:
            try:
                port1 = str(self.port1)
                port2 = str(self.port2)
                if int(port1) > 65355 or int(port1) < 1 or int(port2) > 65355 or int(port2) < 1 or int(port2) <= int(port1):
                        return False
                return True    
                
            except:
                return False        
        
    def startProcess(self):
        port1 = int(self.port1)
        port2 = int(self.port2)
        
        
        sys.stdout.write(f"\n\033[32m[ STARTING PORT SCAN {self.ip}:{self.port1} ] 0%\n\033[0m")
        results = f"\n\nSCANNING RESULT\n---------------\n"
        openPorts = 0
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((self.ip,int(self.port1)))
        
        if result == 0:
            
            
            results += f"|\033[33m{self.port1}: OPEN\033[0m\n"
            openPorts += 1
            
        if result != 0 and port2 == 0:
            
            sys.stdout.write("\033[F\033[K")
            sys.stdout.flush()
            sys.stdout.write(f"\033[32m[ STARTING PORT SCAN {self.ip}:{self.port1} ] 100%\033[0m")
            results = f"\n\nPROCESS CLOSED... {openPorts} port(s) found\n"
            
            
                
            return results     
            
            
        
        if port2 != 0:
                
                portsCount = port2-port1+1
                
                while  port1 < port2:
                    
                    
                    port1 += 1
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
                    result = s.connect_ex((self.ip,int(port1)))
                    if result == 0:
                        results += f"|\033[33m{port1}: OPEN\n\033[0m"
                        openPorts += 1
                    sys.stdout.write("\033[F\033[K")
                    sys.stdout.flush()
                    sys.stdout.write(f"\033[32m[ STARTING PORT SCAN {self.ip}:{port1} ] {round(( 1- (port2-port1)/portsCount ) *100 ,2) }%\n\033[0m")
                        
                        
                sys.stdout.write("\033[F\033[K")
                sys.stdout.flush()
                sys.stdout.write(f"\033[32m[ STARTING PORT SCAN {self.ip}:{port1} ] 100%\033[0m")        
                results += f"\nPROCESS CLOSED... {openPorts} port(s) found from {portsCount} ports\n" 
                
                return results     
        
        sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()
        sys.stdout.write(f"\033[32m[ STARTING PORT SCAN {self.ip}:{self.port1} ] 100%\033[0m")
        results += f"\nPROCESS CLOSED... {openPorts} port(s) found\n"
        
           
            
        return results    
        
                
                                                                                                                                                

m = Menu()
m.displayMenu()
m.displayOptions()
m.getCommand()