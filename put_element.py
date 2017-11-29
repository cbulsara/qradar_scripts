#!/usr/bin/python2.7

import requests
import argparse
import pandas as pd
import json



def initArgParser():                    

    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", help="Provide an API key on the command line.")
    parser.add_argument("-kF", "--keyfile", help="Provide path to a text file that contains the API Key")
    parser.add_argument("-i", "--infile", help="Path to csv input.")
    parser.add_argument("-v", "--value", help="Manually enter value parameter.")
    parser.add_argument("-n", "--name", help="Manually enter name param.")
    parser.add_argument("-s", "--source", help="Manually enter source param.")
    parser.add_argument("-p", "--params", help = "Manually specify params.")

    return parser.parse_args()

def readKeyFile(p):
    f = open(p, "r")
    return f.readline()

def main():
    url = 'https://10.120.40.130/api/reference_data/sets/'
    api_version = '8.0'
    api_token = ''
    args = initArgParser()
    
    if args.key:
        api_token = args.key
    elif args.keyfile:
        api_token = readKeyFile(args.keyfile)
    else:
        print "Please provide an API key."
        quit()
        
    if args.infile:
        print "Not implemented. Use put_bulk.py."
        quit()
    
    if args.params:
        print args.params
        print type(args.params)
        r = requests.post(url + args.name, 
                            verify=False, 
                            headers={'SEC':api_token, 'Version':api_version},
                            params={args.params})
        print r
    
    else:
        r = requests.post(url + args.name, 
                            verify=False, 
                            headers={'SEC':api_token, 'Version':api_version},
                            params={'name':args.name, 'value':args.value, 'source':args.source})
        print r
    
    ##if args.normalize:
    ##   df = pd.io.json.json_normalize(r.json(), args.normalize)
    ##else:
    ##    df = pd.io.json.json_normalize(r.json())
        
    ##df.to_csv(args.outfile)
    ##print df.to_string()

if __name__ == "__main__":
    main()