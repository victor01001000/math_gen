#!/usr/bin/env python3
import sys
import os
import re
import random
import string
import rapid_json
import rapid_ddl
import random_ddl
import time
from multiprocessing import Process

help_text = """
  Rapid Data
  ==========

  Command Line Options:
    Json File:
      -f : path to file
      -n : number of rows
    Random DDL:
      -r : create random ddl and csv file
      -c : number of columns
    Other:
      -a : path to file (append rather than overwriting)
      --help : print help text
  
  Examples:
    ./rapid_data -f json_file.json -n 100
    ./rapid)data -f foo.ddl -n 1000
    ./rapid_data -r -c 10
  
  Default Values:
    int:
      - min: -
      - max: 
    varchar: 
      - min: 0
      - max: 256
"""

options = {
'-f': None,
'-n': 100,
'-c': 10,
'-a': None,
}

options2 = {
'-r': False
}

def parse_command():
  if len(sys.argv) == 1 or '--help' in sys.argv:
     print(help_text)
     sys.exit(0)
  elif '-r' and '-f' not in sys.argv:
     print("ERROR: no file input was provided!")
  else:
    for i in options:
      if i in sys.argv:
        options[i] = sys.argv[sys.argv.index(i)+1]

def read_and_execute():
  try:
    columns = []
    if options2['-r'] == True:
      print("-r not yet supported")
      #random_ddl.RandomDDL(options['-c']) 
    elif options['-f'].endswith(".json"):
      print("json not yet supported")
      #rapid_json.RapidJson(options['-f'])
    elif options['-f'].endswith(".ddl"):
      rapid = rapid_ddl.RapidDDL(options['-f'], options['-n'])
      columns = rapid.read_ddl()
      rapid.generate_rows(columns)
    else:
      print("This file type is not supported")
      exit(1)
  except ValueError:
    print("Unable to find file to read.")
#    exit(1)

def measure_progress():
  print("  Generating data...")
  lines = int(os.popen("wc -l data.csv").read().split()[0])
  while lines < int(options['-n']):
    lines = int(os.popen("wc -l data.csv").read().split()[0])
    progress_output = ("  Lines written: " + str(lines) + "/" + options['-n'])
    print(progress_output, end='\r')
    sys.stdout.flush()
  print("  Finished outputting data to data.csv")

if __name__ == '__main__':
  parse_command()
  Process(target=read_and_execute).start()
  Process(target=measure_progress).start()
