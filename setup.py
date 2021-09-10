import os.path
from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='mkdocs-copy',
    version='0.0.1',
    url='https://github.com/chikamichi/mkdocs-copy',
    license='MIT',
    author='Jean-Denis Vauguet',
    author_email='jd@vauguet.fr',
    description='A mkdocs plugin that lets you copy (and maybe transform) arbitrary doc files to the build.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='mkdocs markdown file copy include export transform',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.0'
    ],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'copy = mkdocs_copy:CopyPlugin'
        ]
    },
)
