from setuptools import setup, find_packages

setup(
    name="toolmenu",
    version="1.0",
    packages=find_packages(),  # will detect 'toolmenu' folder
    entry_points={
        "console_scripts": [
            "toolmenu = toolmenu.main:main"
        ]
    },
    install_requires=["requests"],
    python_requires=">=3.6"
)
