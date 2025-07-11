from setuptools import setup, find_packages

setup(
    name='test',
    version='0.1.0',
    description='Tool Menu CLI',
    author='Outcome9k',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'toolmenu = test.main:main',
        ]
    },
    python_requires='>=3.6',
)
