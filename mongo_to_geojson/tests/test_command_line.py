from mongo_to_geojson.tests.test_config import COLLECTION,MONGO_URI,PIPELINE,QUERY,PROJECTION
from mongo_to_geojson.tests.test_utils import create_parameter_file_input,get_temp_jsonfile_path
from unittest import TestCase
import json
import os
import subprocess


class TestCmd(TestCase):
    def test_collection_dump(self):
        output = get_temp_jsonfile_path()
        cmd = " ".join(['mongo2geojson', MONGO_URI, COLLECTION, output])
        return_code = subprocess.check_call(cmd, shell=True)
        output_created = os.path.exists(output)
        if os.path.exists(output):
            os.remove(output)
        self.assertTrue(return_code == 0)
        self.assertTrue(output_created)

    def test_aggregate_from_jsonfile_no_opts(self):
        pipeline = create_parameter_file_input(PIPELINE)
        output = get_temp_jsonfile_path()
        cmd = " ".join(['mongo2geojson', MONGO_URI, COLLECTION, output, '--agg_pipeline={0}'.format(pipeline)])
        return_code = subprocess.check_call(cmd, shell=True)
        output_created = os.path.exists(output)
        if os.path.exists(output):
            os.remove(output)
        self.assertTrue(return_code == 0)
        self.assertTrue(output_created)

    def test_aggregate_from_jsonstring_no_opts(self):
        output = get_temp_jsonfile_path()
        cmd = " ".join(['mongo2geojson', MONGO_URI, COLLECTION, output, "--agg_pipeline='{0}'".format(json.dumps(PIPELINE))])
        return_code = subprocess.check_call(cmd, shell=True)
        output_created = os.path.exists(output)
        if os.path.exists(output):
            os.remove(output)
        self.assertTrue(return_code == 0)
        self.assertTrue(output_created)

    def test_find_from_jsonfile_with_projection(self):
        query = create_parameter_file_input(QUERY)
        projection = create_parameter_file_input(PROJECTION)
        output = get_temp_jsonfile_path()
        cmd = " ".join(['mongo2geojson', MONGO_URI, COLLECTION, output, '--query={0}'.format(query),
                        '--projection={0}'.format(projection)])
        return_code = subprocess.check_call(cmd, shell=True)
        output_created = os.path.exists(output)
        if os.path.exists(output):
            os.remove(output)
        self.assertTrue(return_code == 0)
        self.assertTrue(output_created)

    def test_find_from_jsonstring_without_projection(self):
        output = get_temp_jsonfile_path()
        cmd = " ".join(['mongo2geojson', MONGO_URI, COLLECTION, output, "--query='{0}'".format(json.dumps(QUERY))])
        return_code = subprocess.check_call(cmd, shell=True)
        output_created = os.path.exists(output)
        if os.path.exists(output):
            os.remove(output)
        self.assertTrue(return_code == 0)
        self.assertTrue(output_created)

    def test_find_from_jsonstring_with_projection(self):
        output = get_temp_jsonfile_path()
        cmd = " ".join(['mongo2geojson', MONGO_URI, COLLECTION, output, "--query='{0}'".format(json.dumps(QUERY)),
                        "--projection='{0}'".format(json.dumps(PROJECTION))])
        return_code = subprocess.check_call(cmd, shell=True)
        output_created = os.path.exists(output)
        if os.path.exists(output):
            os.remove(output)
        self.assertTrue(return_code == 0)
        self.assertTrue(output_created)




