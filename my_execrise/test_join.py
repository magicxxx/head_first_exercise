# -*- coding: utf-8 -*-
from time import time
def method1():
    t = time()
    for i in xrange(100000):
        s = 'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'+'pythontab'

    print time() - t
def method2():
    t = time()
    for i in xrange(100000):
        s = ''.join(['pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab','pythontab'])
    print time() -t
method1()
method2()


