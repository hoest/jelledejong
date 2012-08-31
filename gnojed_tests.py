import os
import gnojed
import unittest
import tempfile

class GnojEdTestCase(unittest.TestCase):
  def setUp(self):
    self.app = gnojed.app.test_client()

  def tearDown(self):
    pass

  def test_baserequest(self):
    rv = self.app.get("/")
    assert "</html>" in rv.data
    assert "<div class=\"main\">" in rv.data

  def test_output(self):
    rv = self.app.get("/test/")
    assert "<h1>Test document</h1>" in rv.data
    assert "<p>This document is <em>used</em> for <strong>test</strong> purposes.</p>" in rv.data

if __name__ == "__main__":
  unittest.main()