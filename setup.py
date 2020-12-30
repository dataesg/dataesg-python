from setuptools import find_packages, setup

INSTALL_REQUIRES = [
    'pandas >= 0.14',
    'numpy >= 1.8',
    'requests >= 2.7.0',
    'matplotlib >= 3.1.3'
]

classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ]


setup(
    name='dataesg',
    packages=['dataesg'],
    version='0.0.2',
    description='Package for dataesg data access',
    Long_description=open('README.md').read(), 
    author='DATAESG',
    author_email='hello@dataesg.com',
    license='MIT',
    url = 'https://github.com/dataesg/dataesg-python',
    download_url = 'https://github.com/dataesg/dataesg-python/archive/v_002.tar.gz',
    keywords=['dataesg', 'data', 'api'],
    classifiers=classifiers,
    install_requires=INSTALL_REQUIRES,
    python_requires='>= 3.5',
)
