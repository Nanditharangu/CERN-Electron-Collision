import yaml


def load_config(file_path = 'config/config.yaml'):
        with open(file_path,'r') as file:
            config = yaml.safe_load(file)

        return config
class Config:
    
    config = load_config()
    data_dir = config['data_dir']
    model_path = config['model_dir']