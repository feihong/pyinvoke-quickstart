from invoke import Collection
from . import main, docs, build

ns = Collection.from_module(main)
for mod in (docs, build):
    ns.add_collection(mod)
