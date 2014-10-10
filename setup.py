from distutils.core import setup
import ripple
setup(name='webi-ripple',
      description='a meta web framework for python',
      url='https://github.com/web-i/ripple',
      version=ripple.__version__,
      packages=['ripple', 'ripple.contrib', 'ripple.adaptors', 'ripple.middlewares', 'ripple.utils', 'ripple.builder'],
      author='Pavan Mishra',
      author_email = 'pavanmishra@gmail.com',
      license='MIT'
      )
