import pickle
from typing import Any


def Picle_data(filename:str,source:Any,):
    '''
    Writes a list of dicts to a JSON file.
    Filename = example.json
    Source = list of dictionaries.
    '''
    outfile = open(filename,'wb')
    pickle.dump(source,outfile)
    outfile.close()