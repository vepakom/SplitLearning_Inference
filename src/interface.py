from algos.split_inference import SplitInference
from algos.nopeek import NoPeek
from data.loaders import DataLoader
from models.model_zoo import Model
from utils.utils import Utils
from utils.config_utils import config_loader


def load_config(filepath):
    return config_loader(filepath)


def load_model(config, utils):
    return Model(config["server"], utils)


def load_data(config):
    return DataLoader(config)


def load_utils(config):
    return Utils(config)


def load_algo(config, utils):
    method = config["method"]
    if method == "split_inference":
        algo = SplitInference(config["client"], utils)
    elif method == "nopeek":
        algo = NoPeek(config["client"], utils)
    else:
        print("Unknown algorithm {}".format(config["method"]))
        exit()

    return algo