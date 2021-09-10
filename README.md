# Copy files in your MkDocs build

mkdocs-copy is a plugin for [MkDocs](https://www.mkdocs.org/) which allows you to copy _verbatim_ arbitrary files in your build.

## Why?

This plugin was created to solve https://github.com/mkdocs/mkdocs/issues/2139 (at least some use-cases affected by it). Basically it's a work-around for the following ([willingly](https://github.com/mkdocs/mkdocs/issues/2139#issuecomment-656659524)) hard-coded chunk in MkDocs' sources:

``` python
# mkdocs/structure/files.py used by 
def get_files(config):
    """ Walk the `docs_dir` and return a Files collection. """
    files = []
    exclude = ['.*', '/templates']

    # ...
```

Note: one could achieve the same result using something like [mkdocs-gen-files](https://oprypin.github.io/mkdocs-gen-files/) or [mkdcos-simple-hooks](https://pypi.org/project/mkdocs-simple-hooks/), only with some more effort. The benefit of using mkdocs-copy dedicated plugin lies in its declarative API. It is also easily reusable.

## Quick start

Say you want to add .htaccess files (if defined for a given folder/path):

``` yaml
# mkdocs.yml config file
plugins:
  - mkdocs-copy:
    add_per_path:
      - .htaccess
```
