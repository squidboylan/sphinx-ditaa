from setuptools import setup, find_packages

setup(
    name='sphinx_ditaa',
    author='Arthur Gautier',
    author_email='aga@zenexity.com',
    description='Sphinx plugin for rendering Ditaa diagrams',
    version='0.0.1',
    install_requires=[
        'setuptools',
        'Sphinx >=1.0.7',
        ],
    packages=find_packages(exclude=['ez_setup']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Documentation',
        'Topic :: Documentation',
        'Topic :: System :: Installation/Setup',
        'License :: OSI Approved :: BSD License',
        ],
    )
