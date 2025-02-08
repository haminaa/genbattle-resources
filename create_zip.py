import os
import zipfile

def zip_directory_except_out(source_dir, out_folder, zip_name):
    out_folder_path = os.path.join(source_dir, out_folder)
    
    if not os.path.exists(out_folder_path):
        os.makedirs(out_folder_path)
    
    zip_path = os.path.join(out_folder_path, zip_name)
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        excluded_files = ['create_zip.py']
        for root, dirs, files in os.walk(source_dir):
            if any(excluded in root for excluded in [out_folder, '.git', 'themes', 'archive']):
                continue
            
            for file in files:
                if file in excluded_files:
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)

            excluded_dirs = {out_folder, '.git', 'themes', 'archive'}
            dirs[:] = [d for d in dirs if d not in excluded_dirs]


def zip_themes(source_directory, out_folder_path):
    themes_dir = os.path.join(source_directory, 'themes')
    out_themes_dir = os.path.join(out_folder_path, 'themes')
        
    if not os.path.exists(out_themes_dir):
        os.makedirs(out_themes_dir)
        
    if os.path.exists(themes_dir):
        for theme_folder in os.listdir(themes_dir):
            theme_folder_path = os.path.join(themes_dir, theme_folder)
            if os.path.isdir(theme_folder_path):
                theme_zip_name = f"{theme_folder}.zip"
                theme_zip_path = os.path.join(out_themes_dir, theme_zip_name)
                    
                with zipfile.ZipFile(theme_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for root, dirs, files in os.walk(theme_folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, theme_folder_path)
                            zipf.write(file_path, arcname)
                    
                print(f"Theme '{theme_folder}' zipped to '{out_themes_dir}/{theme_zip_name}'.")


if __name__ == "__main__":
    source_directory = "./"  # Change this to your directory path
    out_folder_name = "out"
    zip_file_name = "resourcepack.zip"
    out_folder_path = os.path.join(source_directory, out_folder_name)
    zip_directory_except_out(source_directory, out_folder_name, zip_file_name)
    zip_themes(source_directory, out_folder_path)
    print(f"All files zipped to '{out_folder_name}/{zip_file_name}'.")
