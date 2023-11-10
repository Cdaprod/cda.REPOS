from setuptools import setup, find_packages

setup(
    name='cda_repos',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pydantic', 'requests>=2.25.1',
    ],
    entry_points={
        'console_scripts': [
            'cda_repos=cda_repos:main',
        ],
    },
    author='David Cannan',
    author_email='cdaprod@cdaprod.dev',
    description='A tool for managing cda repositories',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    url='https://github.com/cdaprod/cda.repos',  
    classifiers=[
        # Full list: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
