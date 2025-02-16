
import os

source_path = '/path/to/source/file.txt'
destination_path = '/path/to/destination/file.txt'

os.rename(source_path, destination_path)

print(f"File moved from {source_path} to {destination_path}")
