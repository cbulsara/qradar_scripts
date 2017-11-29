#!/usr/bin/python2.7

import requests
import argparse
import pandas as pd
import urllib3

def initArgParser():                    

    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", help="Provide an API key on the command line.")
    parser.add_argument("-kF", "--keyfile", help="Provide path to a text file that contains the API Key")
    parser.add_argument("-i", "--infile", help="Path to csv input.", required=True)
    parser.add_argument("-n", "--name", help="Manually enter name param.")
    

    return parser.parse_args()

def readKeyFile(p):
    f = open(p, "r")
    return f.readline()

def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    args = initArgParser()
    results = [""]
    
    url = 'https://10.120.40.130/api/reference_data/sets/' + args.name
    print "URL = " + url
    api_version = '8.0'
    api_token = ''
    
    if args.key:
        api_token = args.key
    elif args.keyfile:
        api_token = readKeyFile(args.keyfile)
    else:
        print "Please provide an API key."
        quit()
        
    df = pd.read_csv(args.infile)
    
    print "\t\tValue\t\t\tSource\t\t\tName"
    for index, row in df.iterrows():
        r = requests.post(url, 
                            verify=False, 
                            headers={'SEC':api_token, 'Version':api_version},
                            params={'name':row['name'], 'value':row['value'], 'source':row['source']})
        
        
        print str(r.status_code) + "\t\t" + row['value'] + "\t\t" + row['source'] + "\t\t" + row['name']


if __name__ == "__main__":
    main()