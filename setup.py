import setuptools

with open("README.md", "r") as f:
    long_description = f.readlines()

setuptools.setup(
    name='bookworm',
    version='0.0.1',
    author='Bookworm-bit',
    author_email='devworm69@gmail.com',
    description='Collection of random functions that might be useful',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Bookworm-bit/bookworm-pack',
    project_urls={
        "Issues": "https://github.com/Bookworm-bit/bookworm-pack/issues"
        "Website": "https://devworm.tk/"
    },
    license='MIT',
    packages=['bookworm'],
    install_requires=['time'],
)
