#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import CarbeoParser

parser = argparse.ArgumentParser(
    description='Parse a website and save useful informations in a file')
parser.add_argument(
    '--file', '-f', help='path to save our file', required=True)
args = parser.parse_args()

myParser = CarbeoParser.CarbeoParser(
    'http://www.carbeo.com/index.php/prixmoyens', args.file)
