from setuptools import setup, find_packages

setup(
    name="api-speed-test-serverless-20260526_172255",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'api=api:main',
        ],
    },
)
