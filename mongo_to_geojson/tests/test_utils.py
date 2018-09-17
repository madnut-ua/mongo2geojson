from mongo_to_geojson.tests.test_config import COLLECTION, MONGO_URI
from pymongo import MongoClient
import click
import json
import os
import tempfile


def get_temp_jsonfile_path():
    '''
    Returns a valid temp json file path without having created it
    :return:
    '''
    return os.path.join(tempfile.gettempdir(), next(tempfile._get_candidate_names()) + ".json")


def create_parameter_file_input(parameter):
    '''
    creates a temp json file and dumps a parameter into it
    :param parameter: parameter from test_config.py
    :return: file path containing parameter data
    '''
    parameter_file_path = get_temp_jsonfile_path()
    with open(parameter_file_path, 'w') as f:
        json.dump(parameter, f)
    return parameter_file_path

@click.command()
def load_test_data():
    '''
    Atempts to load a Mongo DB with test data using parameters in test_config.  A couple
    of conditions need to be met in order for this to work:
    1.  the collection as specified in test_config.py COLLECTION variable has been exported using
        mongoexport (with --jsonArray flag) into mongo_to_geojson.tests.data folder with naming
        convention COLLECTION.json
    :return:
    '''
    collection_json_array_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data', '{0}.json'.format(COLLECTION))
    with open(collection_json_array_file, 'r') as i:
        data = json.load(i)

    client = MongoClient(MONGO_URI)
    db = client.get_database()
    db[COLLECTION].insert_many(data)


if __name__ == '__main__':
    load_test_data()