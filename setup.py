from distutils.core import setup
from distutils.core import Extension
from Cython.Build import build_ext
from Cython.Build import cythonize
import numpy as np

module1=[ Extension('basic_cython',
          sources=['cython_test_coverage/basic_cython.pyx'],
          language='c')]

if __name__ == "__main__":
     setup( name = 'cython_test_coverage',
            packages=['cython_test_coverage'],
            cmdclass = {'build_ext': build_ext},
            ext_modules = cythonize(module1, compiler_directives={'linetrace': True,'language_level': 3}),
            include_dirs=[np.get_include()],
            description='cython coverage test',
            url='https://github.com/s-sajid-ali/cython_test_coverage',
            author='Sajid',
            author_email='sajidsyed2021@u.northwestern.edu')
