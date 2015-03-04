# kauai

Experimental loader for pulling python functions dynamically from Cassandra.

### Usage

With a schema as in `config/schema.cql`
```
cqlsh> insert into kauai.functions (uuid, content) VALUES ('some_uuid', 'def greet(): print "Hi"')
```

Then in a python interpreter

```python
from kauai import load
load()

from some_uuid import greet as bar

bar()
# Hi
```

Tests require a locally running Cassandra instance, `make test` sets up the schema for the tables.
