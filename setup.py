from setuptools import find_packages, setup


setup(
    name="myapp",
    description="Great app.",
    author="Yakov Wildfluss",
    author_email="yakov@wildfluss.com",
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=["tests*"],
    ),
    entry_points={
        "console_scripts": [
            "myapp=myapp.command_line:main",
        ],
    },
    python_requires=">=3.11",
)
