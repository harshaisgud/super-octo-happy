import unittest
from app import app,parse_args
import os
import subprocess
import json


os.environ['HASH'] = subprocess.getoutput(['git rev-parse HEAD'])
os.environ['APP_NAME'] = 'SplitCamelCase'
class AppTest(unittest.TestCase):

    def test_helloworld(self):
        c = app.test_client(self)
        response = c.get('/helloworld')
        status_code = response.status_code
        self.assertEqual(status_code,200)
        self.assertTrue(b'Hello Stranger' in response.data)

    def test_helloworld_with_query(self):
        c = app.test_client(self)
        response = c.get('/helloworld',query_string={'name': 'HarshaSri'})
        status_code = response.status_code
        self.assertEqual(status_code,200)
        self.assertTrue(b'Harsha Sri' in response.data)
        response2 = c.get('/helloworld',query_string={'name': 'harshaSri'})
        status_code2 = response2.status_code
        self.assertEqual(status_code2,200)
        self.assertTrue(b'harsha Sri' in response2.data)

    def test_versionz(self):
        c = app.test_client(self)
        response = c.get('/versionz')
        status_code = response.status_code
        data = json.loads(response.data)
        self.assertEqual(status_code,200)
        value = subprocess.getoutput(['git rev-parse HEAD'])
        self.assertEqual(str(value), data['hash'])
        self.assertEqual("SplitCamelCase", data["app_name"])



    def test_parse_args(self):
        opts = parse_args(['--port', '3000'])
        port = opts.port
        self.assertEqual(port,3000)

if __name__== '__main__':
    unittest.main()