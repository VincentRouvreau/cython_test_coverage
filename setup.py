from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import build_ext
import numpy as np

ext_modules=[ Extension('basic_cython',
               sources=['cython_test_coverage/basic_cython.pyx'],
                language='c')]

if __name__ == "__main__":
     setup( name = 'cython_test_coverage',
            packages=['cython_test_coverage'],
            cmdclass = {'build_ext': build_ext},
            ext_modules = ext_modules,
            include_dirs=[np.get_include()],
            description='cython coverage test',
            url='https://github.com/s-sajid-ali/cython_test_coverage',
            author='Sajid',
            author_email='sajidsyed2021@u.northwestern.edu',
            zip_safe=False)
