# Gendiff

[![Actions Status](https://github.com/anton-dubrovin/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/anton-dubrovin/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/263f3f927329b50c7753/maintainability)](https://codeclimate.com/github/anton-dubrovin/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/263f3f927329b50c7753/test_coverage)](https://codeclimate.com/github/anton-dubrovin/python-project-50/test_coverage)

## Description
"Gendiff" is a program that determines the difference between two data structures. This is a popular task, for which there are many online services http://www.jsondiff.com/. This is a study project of Hexlet https://ru.hexlet.io/programs/python/projects/50

Utility features:
* Support different input formats: yaml, json
* Report generation as plain text, stylish and json

## Installation
1. Clone the repository to your computer `git clone https://github.com/anton-dubrovin/hexlet-gendiff.git`
2. Go to the project folder `cd hexlet-gendiff`
3. Install the utility `make setup`

## Usage

``` bash
$ gendiff -h
usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output (default: "stylish")
```

## Library
``` python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)
```