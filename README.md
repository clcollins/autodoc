#This repository is archived and will no longer receive updates.

autodoc
=======

Automatic Documentation Generator

Status: **ALPHA** (heavy development)

`autodoc.py` searches the current working directory, recusively, for files that contain `!DOC` and `!COD` tags - similar to `EOF` in bash - and includes the the comments between them in a README.md file.  In this way general documentation can be compiled from an individual document's description.

Bugs
----

* Does not handle absense of !COD tag well

Features to Add
---------------

* Some kind of templating for README.md, or branch and merge so we don't overwrite manually added stuff?
* Read a real config file for config values
* Allow for multiple `!DOC`/`!COD` tags - document functions, etc?
* Parse header of some kind to populate top of README.md
* Add ability to ignore files, set recursion depth

