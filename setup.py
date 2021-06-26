import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Bytrix',
    version='0.1',
    author="Wesley Viana",
    author_email="viana dot wesley at gmail dot com",
    description="My try to a pythonic Bitrix24 rest api wrapper.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wviana/bytrix',
    packages=setuptools.find_packages(),
)
