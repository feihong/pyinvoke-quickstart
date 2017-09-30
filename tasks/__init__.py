"""
In order for Invoke to load your tasks, you must have a variable in this module
named either `ns` or `namespace`.

"""
from invoke import Collection
from . import main, docs, build


namespace = Collection.from_module(main)
for mod in (docs, build):
    namespace.add_collection(mod)
