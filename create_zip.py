import os
import zipfile

def zip_directory_except_out(source_dir, out_folder, zip_name):
    # Full path to the out folder
    out_folder_path = os.path.join(source_dir, out_folder)
    
    # Create out folder if it doesn't exist
    if not os.path.exists(out_folder_path):
        os.makedirs(out_folder_path)
    
    # Path to the ZIP file
    zip_path = os.path.join(out_folder_path, zip_name)
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Skip the "out" folder
            if out_folder in root:
                continue
            
            # Add files and subdirectories to the ZIP file
            for file in files:
                file_path = os.path.join(root, file)
                # Compute the relative path for the ZIP archive
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)

            # Filter out the out folder from dirs to skip walking into it
            dirs[:] = [d for d in dirs if d != out_folder]

if __name__ == "__main__":
    source_directory = "./"  # Change this to your directory path
    out_folder_name = "out"
    zip_file_name = "resourcepack.zip"
    zip_directory_except_out(source_directory, out_folder_name, zip_file_name)
    print(f"All files zipped to '{out_folder_name}/{zip_file_name}'.")
