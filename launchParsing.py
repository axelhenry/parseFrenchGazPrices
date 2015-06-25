#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import yaml

import CarbeoParser

parser = argparse.ArgumentParser(
    description='Parse a website and save useful informations in a file')
parser.add_argument(
    '--conf_file', '-cf',
    help='path to config file, if not provided config.yaml will be used')
# parser.add_argument(
#     '--file', '-f', help='path to save our file', required=True)
args = parser.parse_args()

if args.conf_file:
    with open(args.conf_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
else:
    with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

# myParser = CarbeoParser.CarbeoParser(
#     'http://www.carbeo.com/index.php/prixmoyens', args.file)

myParser = CarbeoParser.CarbeoParser(
    cfg['parser']['url'], cfg['postgresql'])
