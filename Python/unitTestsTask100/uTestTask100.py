import unittest
import calc

class CalcTest(unittest.TestCase):
    '''Calc tests'''
    pass



class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check whether s.split does't work when delimiter is not of a string type      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()