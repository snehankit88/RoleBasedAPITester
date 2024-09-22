from setuptools import setup, find_packages

setup(
    name='RoleBasedAPITester',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'role_based_api_tester=role_based_api_tester.tester:main',
        ],
    },
)
