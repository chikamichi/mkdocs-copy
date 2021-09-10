# Local development (Unix)

## Installing your local plugin clone using pip

``` python
# Inside the cloned repository (/your/path/to/mkdocs-copy/):
python setup.py sdist
pip install mkdocs-copy --no-cache-dir --no-index --find-links file:///your/path/to/mkdocs-copy/dist
```

## Updating your local plugin clone using pip

``` python
# Say python --version is "Python 3.7.3"
rm ~/.local/lib/python3.7/site-packages/mkdocs_copy* -rf
```

Then re-do the steps above (ie. re-installing the local plugin).
