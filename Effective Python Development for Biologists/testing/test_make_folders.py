import os 
from nose.tools import assert_equals 
from nose.tools import with_setup  
 
def make_dirs(n): 
    for i in range(n): 
        os.mkdir(str(i)) 

def remove_folders(): 
    "delete all folders whose name is a single character" 
    for name in os.listdir("."): 
        if len(name) == 1: 
            os.rmdir(name) 
             
@with_setup(teardown=remove_folders) 
def test_make_three_folders(): 
    make_dirs(3) 
    for i in range(3): 
        assert_equals(os.path.exists(str(i)), True) 

