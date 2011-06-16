from attest import Tests

from . import tests
from multicorn import Multicorn



def make_test_suite(make_corn):
    testinstance = Tests()
    def context():
        mc = Multicorn()
        corn = make_corn()
        mc.register(corn)
        yield corn
    testinstance.context(context)
    for test_prototype in dir(tests):
        test_prototype = getattr(tests, test_prototype)
        if hasattr(test_prototype, '_is_corn_test'):
            testinstance.test(test_prototype)
    return testinstance