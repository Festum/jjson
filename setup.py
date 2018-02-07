try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

PACKAGE = 'jjson'
VERSION = '0.0.3'

install_requires = []

def main():
    setup(
        name=PACKAGE,
        version=VERSION,
        description='A library of useful functions to get value from nested JSON',
		long_description=open('README.rst').read(),
        url='https://github.com/festum/jjson',
        author='Festum Qin',
        author_email='festum@g.pl',
        license='MIT',
        py_modules='jjson',
        install_requires=install_requires,
		platforms='any',
		classifiers=[
			'Development Status :: 4 - Beta',
			'Intended Audience :: Developers',
			'License :: OSI Approved :: MIT License',
			'Operating System :: OS Independent',
			'Programming Language :: Python',
			'Programming Language :: Python :: 2',
			'Programming Language :: Python :: 2.5',
			'Programming Language :: Python :: 2.6',
			'Programming Language :: Python :: 2.7',
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.2',
			'Programming Language :: Python :: 3.3',
			'Programming Language :: Python :: 3.4',
			'Programming Language :: Python :: Implementation :: CPython',
			'Programming Language :: Python :: Implementation :: PyPy',
			'Topic :: Software Development :: Libraries :: Python Modules',
		]
    )

if __name__ == '__main__':
    main()
