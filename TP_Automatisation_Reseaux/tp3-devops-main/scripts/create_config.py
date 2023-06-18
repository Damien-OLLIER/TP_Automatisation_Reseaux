import json
from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))


def load_json_data_from_file(file_path):
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
            return(data)
    except FileNotFoundError:
        print("Le fichier {file_path} n'existe pas.")
    pass

def render_network_config(template_name, data):
    template = env.get_template(template_name)
    return(template.render(data))
    

def save_built_config(file_name, data):
    fichier = open(file_name, "w")
    fichier.write(data)
    fichier.close()
    pass

def create_config_cpe_lyon_batA():
    DataR1 = load_json_data_from_file("data/R1_CPE_LYON_BAT_A.json")
    ConfR1A = render_network_config("vlan_router.j2",DataR1)

    DataR2 = load_json_data_from_file("data/R2_CPE_LYON_BAT_A.json")
    ConfR2A = render_network_config("vlan_router.j2",DataR2)

    
    DataESW1 = load_json_data_from_file("data/ESW1_CPE_LYON_BAT_A.json")
    ConfESW1A = render_network_config("vlan_switch.j2",DataESW1)
    return(ConfR1A,ConfR2A,ConfESW1A)

def create_config_cpe_lyon_batB():    
    DataR1 = load_json_data_from_file("data/R1_CPE_LYON_BAT_B.json")
    ConfR1B = render_network_config("vlan_router.j2",DataR1)

    DataR2 = load_json_data_from_file("data/R2_CPE_LYON_BAT_B.json")
    ConfR2B = render_network_config("vlan_router.j2",DataR2)

    
    DataESW1 = load_json_data_from_file("data/ESW1_CPE_LYON_BAT_B.json")
    ConfESW1B = render_network_config("vlan_switch.j2",DataESW1)
    return(ConfR1B,ConfR2B,ConfESW1B)

    
if __name__ == "__main__":
    """
        process question 3 to 5:
    """
    print("begin")
    print("Question 3")
    # Question 3:    
    ConfR1A,ConfR2A,ConfESW1A = create_config_cpe_lyon_batA()
    print('********************')
    print(ConfR1A)
    print('********************')
    print(ConfR2A)
    print('********************')
    print(ConfESW1A)
    print('********************')

    print("")

    # Question 4:
    print("Question 4")
    save_built_config('config/R1_CPE_LYON_BAT_A.conf', ConfR1A)
    save_built_config('config/R2_CPE_LYON_BAT_A.conf', ConfR2A)
    save_built_config('config/ESW1_CPE_LYON_BAT_A.conf', ConfESW1A)

    print("")

    # Question 5:
    print("Question 5")
    ConfR1B,ConfR2B,ConfESW1B = create_config_cpe_lyon_batB()
    save_built_config('config/R1_CPE_LYON_BAT_B.conf', ConfR1B)
    save_built_config('config/R2_CPE_LYON_BAT_B.conf', ConfR2B)
    save_built_config('config/ESW1_CPE_LYON_BAT_B.conf', ConfESW1B)
    
    print("")
    print("done")
    pass