def logincheck(uname,pwd):
    if(uname == 'admin' and pwd =='admin123'):
        return 'success'
    if(uname != 'admin' and pwd =='admin123'):
        return 'fails'
    if(uname == 'admin' and pwd !='admin123'):
        return 'fails'
    if(uname != 'admin' and pwd !='admin123'):
        return 'fails'   
import unittest
class loginclass(unittest.TestCase):
        def test1(self):
            result = logincheck('admin','admin123')
            self.assertEqual(result,'success')
        def test1(self):
            result = logincheck('a','admin123')
            self.assertEqual(result,'fails')
        def test1(self):
            result = logincheck('admin123','admi')
            self.assertEqual(result,'fails')
        def test1(self):
            result = logincheck('ad','m')
            self.assertEqual(result,'fails')
if  __name__ == '__main__':
      unittest.main()

    
   
    




























