#!/usr/bin/env python
import sys

import setuptools as st

sys.path.insert(0, '.')
import version

st.setup(name='path_helpers',
         version=version.getVersion(),
         description='Helper class and functions for working with file path',
         author='Christian Fobel',
         author_email='christian@fobel.net',
         url='http://github.com/cfobel/path_helpers',
         license='MIT License',
         packages=['path_helpers'],
         classifiers=
         ['Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'])
