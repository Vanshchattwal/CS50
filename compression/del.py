import os

# Define the directory path
directory_path = "/workspaces/124705098/compression"

try:
    # List all files in the directory
    files = os.listdir(directory_path)

    # Iterate over the files and delete PNG files
    for file in files:
        if file.endswith(".png"):
            file_path = os.path.join(directory_path, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

    print("All PNG files deleted successfully.")
except OSError as e:
    print(f"Error: {e}")
