
#########################################################

## Pytest :

# Running Pytest can result in six different exit codes:

Exit code 0:	All tests were collected and passed successfully
Exit code 1:	Tests were collected and run but some of the tests failed
Exit code 2:	Test execution was interrupted by the user
Exit code 3:	Internal error happened while executing tests
Exit code 4:	pytest command line usage error
Exit code 5:	No tests were collected

# Commands :

pytest -x            # stop after first failure

pytest test_mod.py   # Run tests in a module

pytest testing/ 	 # Run tests in a directory














