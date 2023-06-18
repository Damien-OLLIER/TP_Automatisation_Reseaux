from nornir import InitNornir

from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result

from nornir_napalm.plugins.tasks import napalm_get, napalm_configure, napalm_cli
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command, netmiko_save_config, netmiko_commit

def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
)

def question_13(nr):
    print(nr.__dict__)
    pass

def question_14(nr):
    print(nr.inventory.hosts)

    inventory = nr.inventory.hosts

    print(type(inventory))

    pass

def question_15(nr):
    print(nr.inventory.hosts.get('R1-CPE-BAT-A'))
    
    print(type(nr.inventory.hosts.get('R1-CPE-BAT-A')))
    pass

def question_16(nr):
    print(nr.inventory.hosts.get('R1-CPE-BAT-A').hostname)
    print(nr.inventory.hosts.get('R1-CPE-BAT-A').username)
    pass

def question_17(nr):
    print("key(): ",nr.inventory.hosts.get('R1-CPE-BAT-A').keys())
    print("room: ",nr.inventory.hosts.get('R1-CPE-BAT-A').data["room"])
    pass

def question_19(nr):
    print(nr.inventory.groups)
    pass

def question_20(nr):
    print(nr.inventory.hosts.get('R1-CPE-BAT-A').groups)
    pass

def question_21(nr):
    print(nr.inventory.hosts.get('R1-CPE-BAT-A').groups[0].keys())
    pass

def question_22(nr):
    print(nr.inventory.hosts.get('R1-CPE-BAT-A').groups[0]["vendor"])
    pass

def question_23(nr):
    for key, value in nr.inventory.hosts.items():
        print("Hostname: ",value)
        print("adresse IP: ",nr.inventory.hosts.get(key).hostname)
        print('')
    pass

def question_24(nr):
    print(nr.filter(device_type="router").inventory.hosts.keys()) 
    pass

def question_25(nr):
    print(nr.filter(device_type="router_switch").inventory.hosts.keys())
    pass

def question_26(nr):
    result = nr.run(task=hello_world)
    print(result)
    print(type(result))
    pass

def question_29():
    command = nr.run(task=hello_world)
    print_result(command)
    pass
    
def question_30():
    command = nr.filter(device_type="router_switch").run(task=hello_world)
    print_result(command)
    pass


def question_32(nr):
    command = nr.filter(device_type="router").run(task=napalm_cli,commands=["sh ip int brief"])
    print_result(command)
    pass
 
def question_33(nr):
    result = nr.filter(device_type="router_switch").run(task=napalm_get,getters=["arp_table"])
    print_result(result)
    pass



if __name__ == "__main__":
    
    nr = InitNornir(config_file="inventory/config.yaml")
    print("")
    print("begin")
    print("")

    # print("Question 13")
    # question_13(nr)

    # print("********")
    # print("Question 14")
    # question_14(nr)

    # print("********")
    # print("Question 15")
    # question_15(nr)
    
    # print("********")
    # print("Question 16")    
    # question_16(nr)

    # print("********")
    # print("Question 17") 
    # question_17(nr)

    # print("********")
    # print("Question 19")    
    # question_19(nr)

    # print("********")
    # print("Question 20")
    # question_20(nr)

    # print("********")
    # print("Question 21")
    # question_21(nr)

    # print("********")
    # print("Question 22")
    # question_22(nr)

    # print("********")
    # print("Question 23")
    # question_23(nr)

    # print("********")
    # print("Question 24")
    # question_24(nr)

    # print("********")
    # print("Question 25")
    # question_25(nr)
    
    # print("********")
    # print("Question 26")
    # question_26(nr)

    # print("********")
    # print("Question 29")
    # question_29()

    # print("********")
    # print("Question 30")
    # question_30()
   
    # print("********")
    # print("Question 32")
    # question_32(nr)

    # print("********")
    # print("Question 33")
    # question_33(nr)

   
    print("")
    print("done")
    print("")
    pass