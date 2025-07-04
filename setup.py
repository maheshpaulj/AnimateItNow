from setuptools import setup, find_packages

setup(
    name='animateitnow',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'openai',
        'manim',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'animateitnow=animateitnow.main:main',
        ],
    },
)