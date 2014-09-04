#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import uuid

if sys.version_info >= (2, 7):
    import unittest
else:
    import unittest2 as unittest

curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, curpath)

import upyun

BUCKET = 'chongwug-pic'
USERNAME = 'chongwug'
PASSWORD = 'weet6321'

BUCKET_TYPE = 'P'


def rootpath():
    return "/pysdk-%s/" % uuid.uuid4().hex


class TestUpYun(unittest.TestCase):

    def setUp(self):
        self.up = upyun.UpYun(BUCKET, USERNAME, PASSWORD, timeout=60,
                              endpoint=upyun.ED_TELECOM, human=False)
        self.root = rootpath()
        self.up.mkdir(self.root)

    def tearDown(self):
        for item in ['test.png', 'test.txt', 'test/test.png', 'test']:
            try:
                self.up.delete(self.root + item)
            except upyun.UpYunServiceException:
                pass
        self.up.delete(self.root)
        with self.assertRaises(upyun.UpYunServiceException) as se:
            self.up.getinfo(self.root)
        self.assertEqual(se.exception.status, 404)

    def test_auth_failed(self):
        with self.assertRaises(upyun.UpYunServiceException) as se:
            upyun.UpYun("bucket", "username", "password").getinfo('/')
        self.assertEqual(se.exception.status, 401)

    def test_client_exception(self):
        with self.assertRaises(upyun.UpYunClientException):
            e = upyun.UpYun("bucket", "username", "password", timeout=3)
            e.endpoint = "e.api.upyun.com"
            e.getinfo('/')

    def test_root(self):
        res = self.up.getinfo('/')
        self.assertDictEqual(res, {'file-type': 'folder'})

    def test_usage(self):
        res = self.up.usage()
        self.assertGreaterEqual(int(res), 0)

    @unittest.skipUnless(BUCKET_TYPE == 'F', "only support file bucket")
    def test_put_directly(self):
        self.up.put(self.root + 'test.txt', 'abcdefghijklmnopqrstuvwxyz\n')
        res = self.up.get(self.root + 'test.txt')
        self.assertEqual(res, 'abcdefghijklmnopqrstuvwxyz\n')
        self.up.delete(self.root + 'test.txt')
        with self.assertRaises(upyun.UpYunServiceException) as se:
            self.up.getinfo(self.root + 'test.txt')
            self.assertEqual(se.exception.status, 404)

    def test_put(self):
        with open('G:/chongwug/chongwug/tests/test.png', 'rb') as f:
            res = self.up.put(self.root + 'test.png', f, checksum=False)
        if BUCKET_TYPE is not 'F':
            self.assertDictEqual(res, {'frames': '1', 'width': '1000',
                                       'file-type': 'PNG', 'height': '410'})
        else:
            self.assertDictEqual(res, {})
        res = self.up.getinfo(self.root + 'test.png')
        self.assertIsInstance(res, dict)
        self.assertEqual(res['file-size'], '13001')
        self.assertEqual(res['file-type'], 'file')
        self.up.delete(self.root + 'test.png')
        with self.assertRaises(upyun.UpYunServiceException) as se:
            self.up.getinfo(self.root + 'test.png')
        self.assertEqual(se.exception.status, 404)

    def test_put_with_checksum(self):
        with open('G:/chongwug/chongwug/tests/test.png', 'rb') as f:
            before = self.up._UpYun__make_content_md5(f)
            self.up.put(self.root + 'test.png', f, checksum=True)
        with open('G:/chongwug/chongwug/tests/get.png', "wb") as f:
            self.up.get(self.root + 'test.png', f)
        with open('G:/chongwug/chongwug/tests/get.png', "rb") as f:
            after = self.up._UpYun__make_content_md5(f)
        self.assertEqual(before, after)
        os.remove('G:/chongwug/chongwug/tests/get.png')
        self.up.delete(self.root + 'test.png')
        with self.assertRaises(upyun.UpYunServiceException) as se:
            self.up.getinfo(self.root + 'test.png')
        self.assertEqual(se.exception.status, 404)

    def test_mkdir(self):
        self.up.mkdir(self.root + 'test')
        res = self.up.getinfo(self.root + 'test')
        self.assertIsInstance(res, dict)
        self.assertEqual(res['file-type'], "folder")
        self.up.delete(self.root + 'test')
        with self.assertRaises(upyun.UpYunServiceException) as se:
            self.up.getinfo(self.root + 'test')
        self.assertEqual(se.exception.status, 404)

    def test_getlist(self):
        self.up.mkdir(self.root + 'test')
        with open('tests/test.png', 'rb') as f:
            self.up.put(self.root + 'test.png', f, checksum=False)
        res = self.up.getlist(self.root)
        self.assertIsInstance(res, list)
        self.assertEqual(len(res), 2)
        if res[0]['type'] is 'F':
            a, b = res[0], res[1]
        else:
            a, b = res[1], res[0]
        self.assertDictEqual(a, {'time': a['time'], 'type': 'F',
                                 'name': 'test', 'size': '0'})
        self.assertDictEqual(b, {'time': b['time'], 'type': 'N',
                                 'name': 'test.png', 'size': '13001'})
        self.up.delete(self.root + 'test')
        self.up.delete(self.root + 'test.png')
        with self.assertRaises(upyun.UpYunServiceException) as se:
            self.up.getlist(self.root + 'test')
        self.assertEqual(se.exception.status, 404)

    def test_delete(self):
        with open('tests/test.png', 'rb') as f:
            self.up.put(self.root + 'test/test.png', f, checksum=False)
        with self.assertRaises(upyun.UpYunServiceException) as se:
            self.up.delete(self.root + 'test')
        self.assertIn(se.exception.status, [503, 403])
        self.up.delete(self.root + 'test/test.png')
        self.up.delete(self.root + 'test')
        with self.assertRaises(upyun.UpYunServiceException) as se:
            self.up.getinfo(self.root + 'test')
        self.assertEqual(se.exception.status, 404)

    def test_put_with_gmkerl(self):
        headers = {"x-gmkerl-rotate": "90"}
        with open('tests/test.png', 'rb') as f:
            res = self.up.put(self.root + 'test.png', f, checksum=False,
                              headers=headers)
        if BUCKET_TYPE is not 'F':
            self.assertDictEqual(res, {'frames': '1', 'width': '410',
                                       'file-type': 'PNG', 'height': '1000'})
        else:
            self.assertDictEqual(res, {})
        self.up.delete(self.root + 'test.png')
        with self.assertRaises(upyun.UpYunServiceException) as se:
            self.up.getinfo(self.root + 'test.png')
        self.assertEqual(se.exception.status, 404)

    def test_handler_progressbar(self):
        class ProgressBarHandler(object):
            def __init__(self, totalsize, params):
                params.assertEqual(totalsize, 13001)
                self.params = params
                self.readtimes = 0
                self.totalsize = totalsize

            def update(self, readsofar):
                self.readtimes += 1
                self.params.assertLessEqual(readsofar, self.totalsize)

            def finish(self):
                self.params.assertEqual(self.readtimes, 3)

        self.up.chunksize = 4096

        with open('tests/test.png', 'rb') as f:
            self.up.put(self.root + 'test.png', f, handler=ProgressBarHandler,
                        params=self)
        with open('tests/get.png', 'wb') as f:
            self.up.get(self.root + 'test.png', f, handler=ProgressBarHandler,
                        params=self)

        self.up.delete(self.root + 'test.png')
        with self.assertRaises(upyun.UpYunServiceException) as se:
            self.up.getinfo(self.root + 'test.png')
        self.assertEqual(se.exception.status, 404)


class TestUpYunHumanMode(TestUpYun):

    def setUp(self):
        self.up = upyun.UpYun(BUCKET, USERNAME, PASSWORD, timeout=60,
                              endpoint=upyun.ED_TELECOM)
        self.root = rootpath()
        self.up.mkdir(self.root)
