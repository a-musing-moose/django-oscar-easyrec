#!/usr/bin/env python
import sys

import logging
logging.disable(logging.CRITICAL)

from argparse import ArgumentParser

import tests.config
from django_nose import NoseTestSuiteRunner


def run_tests(verbosity, *test_args):
    if not test_args:
        test_args = ['tests']
    test_runner = NoseTestSuiteRunner(verbosity=verbosity)
    num_failures = test_runner.run_tests(test_args)
    if num_failures:
        sys.exit(num_failures)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbosity', dest='verbosity', default=1,
                      type=int, help="Verbosity of output")
    options, args = parser.parse_known_args()

    print 'Running tests'
    args += ['-s', '-x']
    run_tests(options.verbosity, *args)
