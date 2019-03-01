# distutils: define_macros=CYTHON_TRACE_NOGIL=1

from distutils.core import setup
from distutils.core import Extension
from Cython.Build import build_ext
import numpy as np




compiler_directives = {}
define_macros = []

compiler_directives['profile'] = True
compiler_directives['linetrace'] = True
define_macros.append(('CYTHON_TRACE', '1')) 


module1=[ Extension('basic_cython',
          sources=['cython_test_coverage/basic_cython.pyx'],
          define_macros=define_macros,
          compiler_directives=compiler_directives
          language='c')]


if __name__ == "__main__":
     setup( name = 'cython_test_coverage',
            packages=['cython_test_coverage'],
            cmdclass = {'build_ext': build_ext},
            ext_modules = module1,
            include_dirs=[np.get_include()],
            description='cython coverage test',
            url='https://github.com/s-sajid-ali/cython_test_coverage',
            author='Sajid',
            author_email='sajidsyed2021@u.northwestern.edu',
            zip_safe=False)
