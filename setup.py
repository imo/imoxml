#!/usr/bin/env python
import os

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

from imoxml.version import __version__

exts = []

# Interface to the Expat XML parser
exts.append(Extension(
        '_imoexpat',
        define_macros=[('HAVE_EXPAT_CONFIG_H', '1')],
        include_dirs=[os.path.join(os.getcwd(), 'modules', 'imoexpat')],
        libraries=[],
        sources=[
            'modules/imoexpat/xmlparse.c',
            'modules/imoexpat/xmlrole.c',
            'modules/imoexpat/xmltok.c',
            'modules/imoexpat/pyexpat.c',
        ]))

# Fredrik Lundh's cElementTree module.  Note that this also
# uses expat (via the CAPI hook in pyexpat).
exts.append(Extension(
        '_imoelementtree',
        define_macros=[
            ('HAVE_EXPAT_CONFIG_H', '1'),
            ('USE_PYEXPAT_CAPI', None),
        ],
        include_dirs=[os.path.join(os.getcwd(), 'modules', 'imoexpat')],
        libraries=[],
        sources=[
            'modules/imoelementtree/_elementtree.c'
        ]))

setup(
    name="imoxml",
    version=__version__,
    author="Patrick Horn",
    author_email="patrick@imo.im",
    maintainer="Patrick Horn",
    maintainer_email="patrick@imo.im",
    url="https://imo.im/",
    description="Improved expat and element tree library for imo.",
    package_dir={'imoxml': 'imoxml'},
    packages=['imoxml', 'imoxml.parsers', 'imoxml.etree'],
    ext_modules=exts,
)
