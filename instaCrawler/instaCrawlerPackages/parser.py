import argparse
import traceback
import json


def parse_args(args):
    try:
        args_dict = vars(args)
        config_path = args_dict['configPath'][0]
        configurations = open(config_path,'r').read()
        config_dict = json.loads(configurations)
        print(config_dict)
    except Exception as exp_obj:
        print(f'Exception : {exp_obj}\n{traceback.format_exc()}')


def main():
    try:
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(help='list of sub parsers')
        new_parser = subparsers.add_parser("start")
        new_parser.set_defaults(func=parse_args)
        new_parser.add_argument("-configPath", nargs='+', required=False, dest="configPath", type=str,
                                action='store', default=["config/config.json"],
                                help="Configuration file path")
        args = parser.parse_args()
        args.func(args)
    except Exception as exp_obj:
        print(exp_obj)
