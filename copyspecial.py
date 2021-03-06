#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Timothy Reynoso with help from Gabby, Leanne, Shanquel, Sondos"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # your code here re.search // match
    path_list = []
    list_files = os.listdir(dirname)
    for file in list_files:
        if re.search(r'__\w*__', file):
            path_list.append(
                os.path.abspath(os.path.join(dirname, file)))
    return path_list


def copy_to(path_list, dest_dir):
    """ given a list of file paths,
    copies those files into the given directory. """
    # your code here
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        shutil.copy(path, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """ given a list of file paths,
    zip those files up into the given zip path """
    # your code here
    subprocess.run(['zip', '-j', dest_zip] + path_list)
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.
    list_paths = get_special_paths(ns.fromdir)
    if ns.todir:
        copy_to(list_paths, ns.todir)
    if ns.tozip:
        zip_to(list_paths, ns.tozip)
    print('\n'.join(list_paths))

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
