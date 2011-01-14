from setuptools import setup, find_packages
import sys, os

version = '0.1'
shortdesc = 'FISE Semantic Engine: RESTful Plone Integration.'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
tests_require = ['interlude']

setup(name='fise.plone',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python', 
            'Topic :: Software Development',       
      ],
      keywords='',
      author='Jens Klein    ',
      author_email='jens@bluedynamics.com',
      url=u'',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
            'setuptools',
            'fise.client',
            'Plone',
      ],
      tests_require=tests_require,
      test_suite="fise.client.tests.test_suite",
      extras_require = dict(
          test=tests_require,
      ),
)
