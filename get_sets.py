#!/usr/bin/python2.7

import requests
import argparse

url = 'https://10.120.40.130/api/'
module = 'reference_data/sets'
api_version = '8.0'

def initArgParser():                    

    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", help="Provide an API key on the command line.")
    parser.add_argument("-kF", "--keyfile", help="Provide path to a text file that contains the API Key")
    return parser.parse_args()

def readKeyFile(p):
    f = open(p, "r")
    return f.readline()

def main():
    
    api_token = ''
    args = initArgParser()
    
    if args.key:
        api_token = args.key
    elif args.keyfile:
        api_token = readKeyFile(args.keyfile)
    else:
        print "Please provide an API key."
        quit()
        
    r = requests.get(url + module, verify=False, headers={'SEC':api_token, 'Version':api_version})

if __name__ == "__main__":
    main()