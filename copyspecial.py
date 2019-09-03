# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys


__author__ = "astephens91"


def get_special_paths(directory):
    """returns a list of the absolute paths of the special files in a dir"""
    result = []
    path_list = os.listdir(directory)  # list path in directory
    for filename in path_list:
        match = re.search(r'__(\w+)__', filename)
        if match:
            result.append(os.path.abspath(os.path.join(directory, filename)))
    return result


def copy_to(path, dir):
    """given a list of paths, copies those files into the given directory"""
    if not os.path.exists(dir):
        os.mkdir(dir)
    for p in path:
        filename = os.path.basename(p)
        shutil.copy(p, os.path.join(dir, filename))


def zip_to(paths, zippath):
    """given a list of paths, zip those files up into the given zipfile"""
    """if file doesn't exist, print error"""
    cmd = ['zip', '-j', zippath]
    print("Command I'm going to do:")
    print('{} {} {}'.format(cmd[0], cmd[1], cmd[2]))
    try:
        cmd.extend(paths)
        subprocess.check_output(cmd)
    except IOError:
        print("zip I/O error: No such file or directory")


def create_parser():
    # Create a cmd line parser with 3 argument defs
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='the directory to read files from')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    # This snippet will help you get started with the argparse module.

    # TODO need an argument to pick up 'from_dir'

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing)
    # with any
    # required args, the general rule is to print a usage message and exit(1).
    if not args:
        parser.print_usage()
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    path_names = []
    for directory in args.from_dir:
        path_names.extend(get_special_paths(directory))
    if args.todir:
        copy_to(path_names, args.todir)
    elif args.tozip:
        zip_to(path_names, args.tozip)
    else:
        print('\n'.join(path_names))


if __name__ == "__main__":
    main()
