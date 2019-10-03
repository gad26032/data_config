#!/usr/bin/env python
"""
usage in the code
from data_config.data_config import *

usage in cli:
    $ data_config/data_config.py [-h] [--action {show_tree,check_data}]

    $ python data_config/data_config.py --action check_data
    $ python data_config/data_config.py --action show_tree

"""
import argparse
import logging
import importlib
import collections

_LOG = logging.getLogger(__name__)

INSTALLED_APPS = [
    'amp.vendors.eurostat',
    'amp.vendors.twitter',
    'some_project.some_module'
]


def init_data():
    g = globals()
    for i in INSTALLED_APPS:
        l = importlib.import_module(f'{i}.data_config')
        for var in l.__dict__.items():
            if isinstance(var[0], str) and var[0] != '_' and var[0] != 'DESCRIPTION':
                g[var[0]] = var[1]


def check_var_names():
    vars_gict = collections.Counter()
    for i in INSTALLED_APPS:
        l = importlib.import_module(f'{i}.data_config')
        for var in l.__dict__.items():
            if isinstance(var[0], str) and var[0][0] != '_' and var[0] != 'DESCRIPTION':
                vars_gict[var[0]] += 1
                if vars_gict[var[0]] > 1:
                    _LOG.error(f'Module "{i}" have not unique var "{var[0]}".')


def check_data_paths():
    vars_gict = collections.Counter()
    for i in INSTALLED_APPS:
        l = importlib.import_module(f'{i}.data_config')
        for var in l.__dict__.items():
            if isinstance(var[0], str) and var[0][1] != '_' and var[0] != 'DESCRIPTION':
                vars_gict[var[0]] += 1
                if vars_gict[var[0]] > 1:
                    _LOG.error(f'Module "{i}" have not unique value {var[1].__repr__()} for variable {var[0]}.')


def show_tree():
    for i in sorted(INSTALLED_APPS):
        print(i)
        l = importlib.import_module(f'{i}.data_config')
        print(f'\tData description: {l.DESCRIPTION}')
        for var in l.__dict__.items():
            if isinstance(var[0], str) and var[0][1] != '_' and var[0] != 'DESCRIPTION':
                print(f'\t{var[0]}={var[1].__repr__()}')
        print('\n')


if __name__ == '__main__':
    ACTIONS = ['show_tree', 'check_data']
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--action', required=False, action='store', choices=ACTIONS, type=str)
    args = parser.parse_args()

    if args.action == 'check_data':
        check_var_names()
        check_data_paths()
    if args.action == 'show_tree':
        show_tree()
else:
    check_var_names()
    check_data_paths()
    init_data()
    g = globals()
    g.pop('argparse')
    g.pop('logging')
    g.pop('importlib')
    g.pop('collections')
    g.pop('_LOG')
    g.pop('INSTALLED_APPS')
    g.pop('init_data')
    g.pop('check_var_names')
    g.pop('check_data_paths')
    g.pop('show_tree')
    g.pop('g')
