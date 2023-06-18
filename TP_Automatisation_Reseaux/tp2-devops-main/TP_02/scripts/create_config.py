import json
from jinja2 import Template, Environment, FileSystemLoader

def load_json_data_from_file(file_path):
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
            return(data)
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'existe pas.")
    pass


def render_network_config(template_name, data):
    template = env.get_template(template_name)
    return(template.render(data))
    pass


def save_built_config(file_name, data):
    fichier = open(f"config/{file_name}", "w")
    fichier.write(data)
    fichier.close()
    pass

def create_vlan_config_cpe_marseille():
    ConfSwitch = render_network_config("vlan_switch.j2", load_json_data_from_file("data/vlan_ESW2.json"))
    ConfRouter = render_network_config("vlan_router.j2", load_json_data_from_file("data/vlan_R02.json"))
    return ConfRouter,ConfSwitch

def create_vlan_config_cpe_paris():
    ConfSwitch = render_network_config("vlan_switch.j2", load_json_data_from_file("data/vlan_ESW4.json"))
    ConfRouter = render_network_config("vlan_router.j2", load_json_data_from_file("data/vlan_R03.json"))
    return ConfRouter,ConfSwitch



if __name__ == "__main__":

    print("** Begin **")

    # Template variable
    env = Environment(loader=FileSystemLoader("templates"))

    # creation of the two configuration for Marseille
    ConfRouterMarseille,ConfSwitchMarseille = create_vlan_config_cpe_marseille()

    # Configuration saving
    save_built_config("ESW2.conf",ConfSwitchMarseille)
    save_built_config("R2.conf",ConfRouterMarseille)

    print("** Conf Marseille DONE **")

    # creation of the two configuration for Paris
    ConfRouterParis,ConfSwitchParis = create_vlan_config_cpe_paris()

    # Configuration saving
    save_built_config("ESW4.conf",ConfSwitchParis)
    save_built_config("R3.conf",ConfRouterParis)

    print("** Conf Paris DONE **")

    print("** End **")

    """
        process question 1 to 5:
    """
    #r02_config, esw2_config = create_vlan_config_cpe_marseille()
    #save_built_config('config/vlan_R02.conf', r02_config)
    #save_built_config('config/vlan_ESW2.conf', esw2_config)
    
    #r03_config, esw4_config = create_vlan_config_cpe_paris()
    #save_built_config('config/vlan_R03.conf', r03_config)
    #save_built_config('config/vlan_ESW4.conf', esw4_config)
