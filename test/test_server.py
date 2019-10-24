"""Tests atlas print server."""

import json
import unittest
import os
import subprocess
from subprocess import PIPE
from os.path import dirname

from qgis_plugin_tools.tools.resources import plugin_test_data_path, metadata_config

__copyright__ = 'Copyright 2019, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'
__revision__ = '$Format:%H$'


class TestServer(unittest.TestCase):

    def test_atlas_capabilities(self):
        """Test GETCAPABILITIESATLAS."""
        env = dict(os.environ)
        path = dirname(dirname(dirname(__file__)))
        query_string = {
            'MAP': plugin_test_data_path('atlas_simple.qgs'),
            'SERVICE': 'WMS',
            'REQUEST': 'GETCAPABILITIESATLAS'
        }
        env['QUERY_STRING'] = ''
        for key in query_string.keys():
            env['QUERY_STRING'] += key + '=' + query_string[key] + '&'
        env['QGIS_PLUGINPATH'] = path

        result = subprocess.run(['qgis_mapserv.fcgi'], env=env, stdout=PIPE, stderr=PIPE)
        result = result.stdout.decode('utf8')
        data = result.split('\n\n')[1]
        result = json.loads(data)
        expected = {
            'status': 'succss',
            'metadata': {
                'name': 'atlasprint',
                'version': metadata_config()['general']['version']
            }
        }
        self.assertDictEqual(result, expected)


if __name__ == '__main__':
    suite = unittest.makeSuite(TestServer)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
