
import json
from napalm import get_network_driver
from jinja2 import Template, Environment, FileSystemLoader

def get_inventory():
    pass


def get_json_data_from_file(file):
    pass


def question_41(device):
    commands = [' show ip int brief']
    output = device.cli(commands)
    print(output)
    device.close()
    pass


def question_42(device):
    commands = [' show ip int brief']
    output = device.cli(commands)
    print(type(output))
    device.close()
    pass

def question_43(device):
    output = device.get_arp_table()
    print(output)
    print(type(output))
    device.close()
    pass


def question_45(device):
    device.load_merge_candidate(filename='config/loopback R01.conf')
    
    print(device.compare_config())# modification entre les configs

    device.commit_config()
    device.close()
    pass

def question_46():

    file_path=["data/ospf_r01.json","data/ospf_r02.json","data/ospf_r03.json"]
    conf_name=["config/ospf_r01.conf","config/ospf_r02.conf","config/ospf_r03.conf"]
    
    for i in range(3):
        with open(file_path[i]) as json_file:
                data = json.load(json_file)
                template = env.get_template("ospf.j2")
                data_template=template.render(data)
                fichier = open(conf_name[i], "w")
                fichier.write(data_template)
                fichier.close()
    pass


def question_47():

    with open("inventory/host.json") as json_file: # on charge les données de l'inventaire
        data = json.load(json_file)
    driver = get_network_driver('ios')

    for i in range(len(data)):
        
        device=data[i]

        if device["hostname"]=="R01" or device["hostname"]=="R02" or device["hostname"]=="R03": # pour eviter les switchs
            print(i)     
            device["hostname"]=device["ip"]           
            device.pop("ip")# erreur si on garde
            device.pop("device_type")# erreur si on garde
            print(device)
            device = driver(**device)
            device.open()
            a=i+1
            result = device.load_merge_candidate(filename=f'config/ospf_r0{a}.conf')
            device.commit_config()# on save
            device.close()# on ferme
            print("done")
            print("")
    pass


if __name__ == "__main__":

    print("")
    print("** Begin **")

    r01 = {
    'hostname': '172.16.100.62',
    'username': 'cisco',
    'password': 'cisco'
    } 
    driver = get_network_driver('ios')
    device = driver(**r01)
    device.open()

    # print("")
    # print("** question 41 **")
    # question_41(device)

    # print("")
    # print("** question 42 **")
    # question_42(device)

    # print("")
    # print("** question 43 **")
    # question_43(device)  

    # print("")
    # print("** question 45 **")
    # question_45(device) 
    
    # print("")
    # print("** question 46 **")
    # env = Environment(loader=FileSystemLoader("templates"))
    # question_46()  

    # print("")
    # print("** question 47 **")
    # env = Environment(loader=FileSystemLoader("templates"))
    # question_47()  

    # print("")
    # print("** End **")
    # print("")

    pass
        