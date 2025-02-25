import zipfile
import os

def compress_file(input_file, output_zip):
    """Compress a file into a .zip archive."""
    try:
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(input_file, os.path.basename(input_file))
        print(f"File {input_file} compressed successfully into {output_zip}")
    except Exception as e:
        print(f"Error: {e}")

def compress_directory(input_directory, output_zip):
    """Compress all files in a directory into a .zip archive."""
    try:
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for folder_name, subfolders, filenames in os.walk(input_directory):
                for filename in filenames:
                    file_path = os.path.join(folder_name, filename)
                    arcname = os.path.relpath(file_path, input_directory)
                    zipf.write(file_path, arcname)
        print(f"Directory {input_directory} compressed successfully into {output_zip}")
    except Exception as e:
        print(f"Error: {e}")
