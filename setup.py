from setuptools import setup


setup(
    entry_points={
        'console_scripts': [
            'ocid_precommit_check = ocid_precommit_check:main',
        ],
    },
)
