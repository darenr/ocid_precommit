from setuptools import setup

setup(
    name="ocidscanner",
    description="Check for ocids in precommit hook",
    url="https://github.com/darenr/ocid_precommit",
    version="1.0.0",
    scripts=["check_ocid/ocidscanner"],
)
