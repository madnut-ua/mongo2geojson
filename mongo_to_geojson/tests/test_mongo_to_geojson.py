from mongo_to_geojson import mongo_to_geojson
from mongo_to_geojson.tests.test_config import COLLECTION,MONGO_URI,PIPELINE,QUERY,PROJECTION
from mongo_to_geojson.tests.test_utils import get_temp_jsonfile_path
from unittest import TestCase
import os
import json


class TestMongoToGeoJson(TestCase):

    def test_collection_dump(self):
        output = get_temp_jsonfile_path()
        mongo_to_geojson(MONGO_URI,'cities',output)
        output_created = os.path.exists(output)
        if output_created:
            os.remove(output)
        self.assertTrue(output_created)


    def test_aggregate(self):
        output = get_temp_jsonfile_path()
        mongo_to_geojson(MONGO_URI,COLLECTION,output,pipeline=PIPELINE)
        output_created = os.path.exists(output)
        if output_created:
            os.remove(output)
        self.assertTrue(output_created)

    def test_find_without_projection(self):
        output = get_temp_jsonfile_path()
        mongo_to_geojson(MONGO_URI,COLLECTION,output,query=QUERY)
        output_created = os.path.exists(output)
        if output_created:
            os.remove(output)
        self.assertTrue(output_created)

    def test_find_with_projection(self):
        output = get_temp_jsonfile_path()
        mongo_to_geojson(MONGO_URI,COLLECTION,output,QUERY,PROJECTION)
        output_created = os.path.exists(output)
        if output_created:
            with open(output,'r') as o:
                feature_collection = json.load(o)
                first_feature = feature_collection['features'][0]
                property_count = len(list(first_feature['properties'].keys()))
            os.remove(output)

        self.assertEqual(property_count,3)