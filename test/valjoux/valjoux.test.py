import time

from valjoux import Eta


def test():
    eta = Eta(log=True)
    eta.ini('begin')
    time.sleep(0.4)
    eta.lap('slept')
    time.sleep(0.3)
    eta.end('finale')


test()
