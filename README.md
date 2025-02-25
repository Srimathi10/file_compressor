
```markdown
# File Compressor

A Python package that compresses files into `.zip` format. This package provides a simple way to compress single files into a zip archive using Python.

## Features

- Compress a single file into a `.zip` archive.
- Easy-to-use API with minimal code.
- Simple and effective file compression utility.

## Installation

You can install the `file_compressor` package via pip. Open your terminal and run the following command:

```bash
pip install file-compressor
```

## Usage

After installing the package, you can use it to compress files into `.zip` archives. Here's an example of how to use it in your Python script:

```python
from file_compressor import compress_file

# Specify the file you want to compress
input_file = 'path/to/your/file.txt'
output_file = 'path/to/output/file.zip'

# Compress the file
compress_file(input_file, output_file)
```

### Example:

```python
from file_compressor import compress_file

compress_file('documents/sample.txt', 'archives/sample.zip')
```

This will compress the `sample.txt` file located in the `documents` directory into a `.zip` archive called `sample.zip` in the `archives` directory.

## Contributing

Contributions are welcome! If you find any issues or want to add a new feature, feel free to open an issue or a pull request.

### Steps to contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Links

- GitHub repository: [https://github.com/Srimathi10/file_compressor](https://github.com/Srimathi10/file_compressor)
- PyPi page: [https://pypi.org/project/file-compressor/](https://pypi.org/project/file-compressor/)

---

### **Changelog**
- **0.1.0**: Initial release.
```
