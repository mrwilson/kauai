REQUIREMENTS := ./requirements.txt
SCHEMA := ./config/schema.cql
PROJECT := kauai

build: deps test
	@python setup.py install

test: deps
	@nosetests --nocapture

deps:
	@pip install -q -r $(REQUIREMENTS)
	@cqlsh -f $(SCHEMA)

clean:
	@find . -name '*.pyc' | xargs rm -f
	@rm -rf $(PROJECT).egg-info dist build
