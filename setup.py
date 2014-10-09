from distutils.core import setup
import ripple
setup(name='webi',
      version=ripple.__version__,
      packages=['ripple', 'ripple.contrib', 'ripple.adaptors', 'ripple.middlewares', 'ripple.utils'],
      author='Pavan Mishra',
      license='MIT',
      platforms=['any']
      )
