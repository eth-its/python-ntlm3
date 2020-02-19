from setuptools import setup


setup(name='python-ntlm3-eth-its',
    version='1.0.3',
    description='Python 3 compatible NTLM library',
    long_description="""
    This package allows Python clients running on any operating
    system to provide NTLM authentication to a supporting server.
    """,
    author='Matthijs Mullender',
    author_email='info@zopyx.org',
    maintainer='Graham Pugh',
    maintainer_email='g.r.pugh+github@gmail.com',
    url="https://github.com/eth-its/python-ntlm3",
    packages=["ntlm3"],
    zip_safe=False,
    license="GNU Lesser GPL",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    install_requires=[
        "six"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',      )
