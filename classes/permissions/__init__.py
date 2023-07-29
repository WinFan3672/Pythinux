#!/usr/bin/python
import pythinux
class Permission(pythinux.Fuse):
    pass
class Storage(pythinux.Base):
    def __init__(self):
        self.read = Permission()
class permissions(pythinux.Base):
    def __init__(self):
        self.storage = Storage()
