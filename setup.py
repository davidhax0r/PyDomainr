from setuptools import setup

setup(name='pydomainr',
      version='0.2',
      description='Python wrapper for the domai.nr API',
      url='http://github.com/itsnauman/PyDomainr',
      author='Nauman Ahmad',
      author_email='nauman-ahmad@outlook.com',
      license='MIT',
      packages=['pydomainr'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
