import json

import pandas as pd
from elasticsearch import Elasticsearch
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Index into Elasticsearch using this script")
    parser.add_argument('-e', '--es', dest='es', default="http://localhost:9209", help='host target')
    args = parser.parse_args()

    if args.es:
        host = args.es

    print('host - ', host)