import os, sys
import argparse
from pathlib import Path

from system.extras import InitializeNewAccount


parser = argparse.ArgumentParser()
parser.add_argument("new_account", help="Creating a new account", type=str)

args = parser.parse_args()


if args.new_account:
    InitializeNewAccount()
else:
    print("Command Does not Exist")