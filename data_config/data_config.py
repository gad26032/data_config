import argparse
import logging
import importlib

_LOG = logging.getLogger(__name__)

INSTALLED_APPS = [
    'amp.vendors.eurostat',
    'amp.vendors.twitter',
    'some_project.some_module'
]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--version', required=False, action='store', type=str)
    parser.add_argument('--version', required=False, action='store', type=str)
    parser.add_argument('--version', required=False, action='store', type=str)
    parser.add_argument('--version', required=False, action='store', type=str)
    args = parser.parse_args()


# todo unique check
# todo
# todo
# todo
# todo
# todo
# todo
