#!/usr/bin/env python

# Copyright (c) 2018 Red Hat, Inc.
# All Rights Reserved.

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="ansible-runner-http",
    version="1.0.0",
    author="Red Hat Ansible",
    url="https://github.com/ansible/ansible-runner-http",
    license='Apache',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
        'requests-unixsocket',
    ],
    entry_points={'ansible_runner.plugins': 'http = ansible_runner_http'},
    zip_safe=False,
)
