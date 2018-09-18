import unittest
from dsopztest import abstract_test_case
from dsopz import datastore as ds
import json as JSON

class TestCase(abstract_test_case.TestCase):

    def test_run_query(self):

        result = ds.run_query('dsopzproj', '', 'select * from notfound where x = 2 and y = 1')
        self.assertEqual(0, len(result['batch']['entityResults']))
        self.assertEqual('NO_MORE_RESULTS', result['batch']['moreResults'])
        self.assertIsNotNone(result['batch']['endCursor'])

        result = ds.run_query('dsopzproj', '', result['query'])
        self.assertEqual(0, len(result['batch']['entityResults']))
        self.assertEqual('NO_MORE_RESULTS', result['batch']['moreResults'])
        self.assertIsNotNone(result['batch']['endCursor'])

        result = ds.run_query('dsopzproj', '', result['query'])
        self.assertEqual(0, len(result['batch']['entityResults']))
        self.assertEqual('NO_MORE_RESULTS', result['batch']['moreResults'])
        self.assertIsNotNone(result['batch']['endCursor'])

    def test_full(self):

        entity = {
            'key': {
                'partitionId': { 'projectId': 'dsopzproj' },
                'path': [ { 'kind': 'hero', 'name': 'ana' }]
            },
            'properties': {
                'role': { 'stringValue': 'SUPPORT' }
            }
        }

        #loaded = ds.lookup('dsopzproj', [ entity['key'] ])
        #self.assertEqual(entity, loaded['found'][0]['entity'])
        #self.assertEqual(0, len(loaded['found']))
        #self.assertEqual(1, len(loaded['missing']))

        result = ds.run_query('dsopzproj', '', 'select * from hero')
        self.assertEqual(entity, result['batch']['entityResults'][0]['entity'])
        self.assertEqual(1, len(result['batch']['entityResults']))
        self.assertEqual('NO_MORE_RESULTS', result['batch']['moreResults'])
        self.assertIsNotNone(result['batch']['endCursor'])

        loaded = ds.lookup('dsopzproj', [ entity['key'], {
            'partitionId': { 'projectId': 'dsopzproj' },
            'path': [ { 'kind': 'notfound', 'name': 'notfound' } ]
        } ])
        self.assertEqual(entity, loaded['found'][0]['entity'])
        self.assertEqual(1, len(loaded['found']))
        self.assertEqual(1, len(loaded['missing']))

if __name__ == '__main__':
    unittest.main()