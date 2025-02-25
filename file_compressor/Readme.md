# File Compressor

This package allows you to compress files and directories into zip archives using simple Python functions.

## Installation

To install this package from PyPi:

pip install file_compressor


## Usage

To compress a file:

```python
from file_compressor import compress_file

compress_file('example.txt', 'output.zip')


To compress a directory:

from file_compressor import compress_directory

compress_directory('example_folder', 'output_folder.zip')
