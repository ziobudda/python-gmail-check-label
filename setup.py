from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gmail-label-checker",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to check and create Gmail labels using OAuth2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gmail-label-checker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "google-api-python-client>=2.0.0",
        "google-auth-oauthlib>=0.4.0",
        "google-auth-httplib2>=0.1.0",
    ],
    entry_points={
        "console_scripts": [
            "gmail-label-checker=check_label:main",
        ],
    },
    package_data={
        "": ["credentials-sample.json"],
    },
    include_package_data=True,
)
