.PHONY: test
test:
	nosetests --verbose --with-coverage

install:
	python setup.py install

requirements:
	pip freeze | grep -v ingest > requirements.txt

clean:
	rm -rf ingest.egg-info build dist
	find ingest -name '*.pyc' | xargs --no-run-if-empty rm -f
