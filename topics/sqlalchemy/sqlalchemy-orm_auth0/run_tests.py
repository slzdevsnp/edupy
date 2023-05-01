import unittest, os,sys

script_directory = os.path.dirname(os.path.abspath(__file__))
projroot_directory = script_directory
sys.path.extend([os.path.join(projroot_directory, 'examples')])



def main():
    # Discover all tests in the "tests" directory
    test_dir = os.path.join(projroot_directory, 'tests')
    loader = unittest.TestLoader()
    test_suite = loader.discover(start_dir=test_dir, pattern='*_test.py')

    # Run the discovered tests
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)


if __name__ == "__main__":
    main()