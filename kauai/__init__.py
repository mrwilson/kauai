import contextlib, imp, os, sys
from cassandra.cluster import Cluster

class KauaiLoader(object):
    def __init__(self):
	self.session = Cluster().connect('kauai')

    @classmethod
    def find_module(cls, name, path=None):
        return cls()

    def load_module(self, name):
        if name in sys.modules: return sys.modules[name]

        mod = imp.new_module(name)
	out = self.session.execute("select content from functions where uuid='%s'" % name)
        if len(out) == 0:
          return None

	exec out[0].content in mod.__dict__

        sys.modules[name] = mod
        return mod

@contextlib.contextmanager
def imports():
    try:
        sys.meta_path.append(KauaiLoader)
        yield
    finally:
        sys.meta_path.remove(KauaiLoader)

def load():
  sys.meta_path.append(KauaiLoader)
