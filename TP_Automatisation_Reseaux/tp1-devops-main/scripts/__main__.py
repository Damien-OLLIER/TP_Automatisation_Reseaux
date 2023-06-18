import json
import yaml
from jinja2 import Template, Environment, FileSystemLoader

def load_json_data_from_file(file_path):
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
            return(data)
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'existe pas.")
    pass


def from_json():
    f = open('data/R2.json') # Opening JSON file
    data = json.load(f) # returns JSON object as a dict
    template = env.get_template("R2.j2")
    print(template.render(data))


def load_yaml_data_from_file(file_path):
    try:
        with open(file_path) as yaml_file:
            data = yaml.safe_load(yaml_file)
    except FileNotFoundError:
        print(f"ERREUR | Le fichier {file_path} n'existe pas.")
    return data
    


def render_network_config(template_name, data):
    template = env.get_template(template_name)
    return(template.render(data))


#print(render_network_config("R2.j2", load_json_data_from_file("data/R2.json")))

def save_built_config(file_name, data):
    fichier = open(f"config/{file_name}", "w")
    fichier.write(data)
    fichier.close()
    pass

if __name__ == "__main__":

    env = Environment(loader=FileSystemLoader("templates"))

    save_built_config("ESW2.conf",render_network_config("ESW2.j2", load_json_data_from_file("data/ESW2.json")))
    save_built_config("R2.conf",render_network_config("R2.j2", load_json_data_from_file("data/R2.json")))

    save_built_config("ESW4_from_yaml.conf",render_network_config("ESW2.j2", load_yaml_data_from_file("data/ESW4.yaml")))
    save_built_config("R2.conf",render_network_config("R2.j2", load_yaml_data_from_file("data/R2.yaml")))

    print(load_yaml_data_from_file("data/ESW4.yaml"))
    print(render_network_config("R2.j2", load_yaml_data_from_file("data/R2.yaml")))
    pass

