import unittest, sys
from nose.tools import istest as test
from nose.tools import raises
from kauai import KauaiLoader

class KauaiLoaderTest(unittest.TestCase):

  @test
  def shouldIgnoreLoaderIfModuleExists(self):
    sys.modules['foo'] = 'bar'
    loader = KauaiLoader()
    assert loader.load_module('foo') == 'bar'
