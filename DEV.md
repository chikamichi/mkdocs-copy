# Local development (Unix)

## Installing your local plugin clone using pip

``` python
# Install projects' dependencies
python[3] setup.py install

# Inside the cloned repository (/your/path/to/mkdocs-copy/):
python[3] setup.py sdist
pip[3] install mkdocs-copy --no-cache-dir --no-index --find-links file:///your/path/to/mkdocs-copy/dist
```

## Updating your local plugin clone using pip

``` python
# Say python --version is "Python 3.7.3"
rm ~/.local/lib/python3.7/site-packages/mkdocs_copy* -rf
```

Then re-do the steps above (ie. re-installing the local plugin).
