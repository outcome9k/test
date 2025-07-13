from setuptools import setup, find_packages

setup(
    name="toolmenu",
    version="1.0",
    author="outcome9k",
    description="CLI tool to manage and run obfuscation tools from GitHub",
    packages=find_packages(),  # Finds 'test' package
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "toolmenu = test.main:main"  # maps 'toolmenu' command to main() in test/main.py
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
)
