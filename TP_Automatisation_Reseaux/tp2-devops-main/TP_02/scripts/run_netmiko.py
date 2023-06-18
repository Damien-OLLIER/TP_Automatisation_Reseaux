from traceback import print_tb
from netmiko import ConnectHandler
import json

def question_25(net_connect):
    command = "show ip int brief"

    with ConnectHandler(**r01) as net_connect:
        output = net_connect.send_command(command)

    # Automatically cleans-up the output so that only the show output is returned
    print()
    print(output)
    print()
    pass


def question_26(net_connect):
    command = "show ip int brief"

    with ConnectHandler(**r01) as net_connect:
        output = net_connect.send_command(command, use_textfsm=True)

    # Automatically cleans-up the output so that only the show output is returned
    print()
    print(output)
    print()
    pass



def question_27(net_connect):
    command = "show ip route"
    with ConnectHandler(**r01) as net_connect:
        output = net_connect.send_command(command, use_textfsm=True)

    # Automatically cleans-up the output so that only the show output is returned
    print()
    print(output)
    print()
    pass


def question_28(net_connect):
    command = "show ip int brief"

    with ConnectHandler(**r01) as net_connect:
        output = net_connect.send_command(command, use_textfsm=True)

    #Automatically cleans-up the output so that only the show output is returned
 
    i = 0
    while i < len(output): 
        InterfaceName = output[i]["intf"]
        command = "sh ip interface {}".format(InterfaceName)
        
        with ConnectHandler(**r01) as net_connect:
            InterfaceConfiguration = net_connect.send_command(command, use_textfsm=True)

        print('** Interface {} **'.format(InterfaceName))
        print(" ")
        print(InterfaceConfiguration)
        print(" ")
        print("** END Interface **")
        print(" ")

        i = i+1    
    pass


def question_29(net_connect):
    command = ['interface loopback1','ip address 192.168.1.1 255.255.255.255','description loopback interface from netmiko']
    with ConnectHandler(**r01) as net_connect:
        output = net_connect.send_config_set(command)
        output += net_connect.save_config()
    
    print("")
    print(output)
    print("")
    pass


def question_30(net_connect):
    command = ['interface loopback1','no interface loopback 1']
    with ConnectHandler(**r01) as net_connect:
        output = net_connect.send_config_set(command)
        output += net_connect.save_config()
    
    print("")
    print(output)
    print("")
    pass


def question_31(net_connect):
    cfg_file = "config/loopback_R01.conf"
    with ConnectHandler(**r01) as net_connect:
            output = net_connect.send_config_from_file(cfg_file)
            output += net_connect.save_config()
    
    print("")
    print(output)
    print("")
    pass


def question_32(net_connect):
    cfg_file = "config/loopback_R01_Erase.conf"
    with ConnectHandler(**r01) as net_connect:
            output = net_connect.send_config_from_file(cfg_file)
            output += net_connect.save_config()
    
    print("")
    print(output)
    print("")
    pass


def get_inventory():
    file_path='inventory/host.json'
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Erreure, Le fichier {file_path} n'existe pas.")
    pass


def question_35():
    data = get_inventory()
    i=0
    while i < len(data):

        InterfaceName = data[i]["hostname"]
        ip = data[i]["ip"]
        device_type = data[i]["device_type"]
        username = data[i]["username"]
        password = data[i]["password"]

        if(InterfaceName.__contains__('R')):
            print(InterfaceName)
            # print(ip)
            # print(device_type)
            # print(username)
            # print(password)

            command = "sh ip interface GigabitEthernet0/0.99"
            with ConnectHandler( device_type = device_type, host=ip, username=username, password = password) as net_connect:
                InterfaceConfiguration = net_connect.send_command(command, use_textfsm=True)

            # with ConnectHandler(InterfaceName,ip,device_type,username,password) as net_connect:
            #     InterfaceConfiguration = net_connect.send_command(command, use_textfsm=True)
                
            print(InterfaceConfiguration)
        i+=1
    
    pass

def question_36():

    data = get_inventory()
    i=0
    while i < len(data):
        InterfaceName = data[i]["hostname"]
        ip = data[i]["ip"]
        device_type = data[i]["device_type"]
        username = data[i]["username"]
        password = data[i]["password"]     

        if(InterfaceName == "R03"):
            print("beginning of R03 configuration")
            cfg_file = "config/R3.conf"
            with ConnectHandler(device_type = device_type, host=ip, username=username, password = password) as net_connect:
                output = net_connect.send_config_from_file(cfg_file)
                output += net_connect.save_config()
            print(output)
            print("")
            print("Configuration for Router R03 has been sent")
            print("")

            
        if(InterfaceName == "R02"):
            print("beginning of R02 configuration")
            cfg_file = "config/R2.conf"
            with ConnectHandler(device_type = device_type, host=ip, username=username, password = password) as net_connect:
                output = net_connect.send_config_from_file(cfg_file)
                output += net_connect.save_config()
            print(output)
            print("")
            print("Configuration for Router R02 has been sent")
            print("")
            
        if(InterfaceName == "S02"):
            print("beginning of S02 configuration")
            cfg_file = "config/ESW2.conf"
            with ConnectHandler(device_type = device_type, host=ip, username=username, password = password) as net_connect:
                output = net_connect.send_config_from_file(cfg_file)
                output += net_connect.save_config()
            print(output)
            print("")
            print("Configuration for Switch S02 has been sent")
            print("")
        
        if(InterfaceName == "S04"):
            print("beginning of S04 configuration")
            cfg_file = "config/ESW4.conf"
            with ConnectHandler(device_type = device_type, host=ip, username=username, password = password) as net_connect:
                output = net_connect.send_config_from_file(cfg_file)
                output += net_connect.save_config()
            print(output)  
            print("")          
            print("Configuration for Switch S04 has been sent")
            print("")

        i+=1

    pass
      

if __name__ == "__main__":  
    print("")
    print("** Begin **")

    r01 = {
    'device_type': 'cisco_ios',
    'host': '172.16.100.62',
    'username': 'cisco',
    'password': 'cisco'
    }  
    

    net_connect = ConnectHandler(**r01) 

   
    #question_25(net_connect)
    #question_26(net_connect)
    #question_27(net_connect)
    #question_28(net_connect)
    #question_29(net_connect)
    #question_30(net_connect)
    #question_31(net_connect)
    #question_32(net_connect)
    
    # data = get_inventory()
    # print(data)
    
    #question_35()
    question_36()



    # Show command that we execute.
    #command = "show ip int brief"
    

    
    
    print("** End **")
    print("")

    pass