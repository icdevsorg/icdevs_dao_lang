import os
import shutil

def inject_front_matter(src_folder, dest_folder):
    for subdir, dirs, files in os.walk(src_folder):
        for filename in files:
            filepath = os.path.join(subdir, filename)
            # Determine the new path based on the destination folder
            rel_path = os.path.relpath(filepath, src_folder)
            new_path = os.path.join(dest_folder, rel_path)

            # Ensure the destination directory exists
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            if filepath.endswith(".md"):
                with open(filepath, 'r') as file:
                    content = file.read()
                
                # Extract the title from the first line of the file
                first_line = content.split('\n', 1)[0]
                title = first_line.replace('# ', '').strip()
                title = title.replace('## ', '').strip()
                
                # Create the front matter
                front_matter = f"---\nlayout: home\ntitle: {title}\n---\n\n"
                
                # Combine the front matter with the original content
                new_content = front_matter + content
                
                # Determine the new path based on the destination folder
                rel_path = os.path.relpath(filepath, src_folder)
                new_path = os.path.join(dest_folder, rel_path)
                
                # Ensure the destination directory exists
                os.makedirs(os.path.dirname(new_path), exist_ok=True)
                
                # Write the new content to the destination path
                with open(new_path, 'w') as new_file:
                    new_file.write(new_content)
                print(f"Processed {new_path}")
            else:
                # Copy other file types as is
                shutil.copy2(filepath, new_path)

# Specify the source and destination directories
src_folder = 'content'
dest_folder = '.'  # Current directory as root

inject_front_matter(src_folder, dest_folder)