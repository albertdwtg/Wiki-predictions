run-local-tests:
	pytest data-collection/test_main.py

reorganize-python-code:
	autopep8 --in-place --aggressive --aggressive data-collection/test_main.py
	autopep8 --in-place --aggressive --aggressive data-collection/main.py

		