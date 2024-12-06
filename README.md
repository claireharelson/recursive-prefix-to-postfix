# Lab 2

This python package is designed to accept prefix statements and convert them to postfix form using recursion.


* Pycharm IDE was used for running this package, information as follows:

PyCharm 2022.3.2 (Community Edition)
Build #PC-223.8617.48, built on January 24, 2023
Runtime version: 17.0.5+1-b653.25 x86_64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
macOS 13.2
GC: G1 Young Generation, G1 Old Generation
Memory: 1024M
Cores: 8
Metal Rendering is ON
Non-Bundled Plugins:
    com.leinardi.pycharm.pylint (0.14.0)

* A Macintosh operating system Ventura 13.2 was used.


## Running Lab2

1. Download and install python on your computer
2. Run the program in the terminal as a module: python -m Lab2_package <input_file> <output_file>


### Lab2 Usage:

usage: python -m Lab2 [-h] in_file out_file

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

* make sure input file path is correct to successfully run the program. Will be located ~/Lab2/Lab2_package/<input>

optional arguments:
  -h, --help  show this help message and exit


## Project Layout:

- Lab2/: The parent folder holding all the project files
  - README: This guide the user is currently reading. Explains package usage
  - Lab2_package: The main module within the package
    - __init__.py: Used to show what functions, variables, classes, etc are exposed when scripts import this module.
    - __main__.py: The entrypoint to the program when ran as a program. 
    - runtime_metrics.py: Creates a class to measure runtime metrics
    - str_converter.py: Creates a function to convert prefix strings to postfix strings recursively
    - lab2.py: Defines functions to take input and output files to process
    - required_input.txt: Required input file (contains issues that raise specific assertion errors)
    - input1.txt: Contains all the properly formatted items from the 'required_input' file to demonstrate successful
        overall program execution
    - input2.txt: Contains items in lower case/mixed case to demonstrate ability of code to handle this type of input
      and convert to uppercase output
    - input3.txt: Other example inputs that contain spaces, blank lines, other variables, incorrect operand to
        operator ratios
    - output(#).txt: Empty text files to write data to through program execution
