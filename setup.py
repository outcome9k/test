from setuptools import setup, find_packages
from test.main import main
setup(
    name='test',
    version='0.1.0',
    description='Example CLI Obfuscator Tool Menu',
    author='Outcome9k',
    author_email='you@example.com',
    url='https://github.com/outcome9k/test',
    packages=find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'toolmenu = test.main:main',  # <command> = <module>:<function>
        ]
    },
)
