import os
import re

def ensure_bullets_in_section(content, section_title):
    section_regex = re.compile(rf"(### {section_title}.*?)(### |\Z)", re.DOTALL)
    matches = section_regex.findall(content)
    
    if not matches:
        return content  # Return original content if section not found

    updated_content = content
    for match in matches:
        section, next_section = match
        updated_section = []
        for line in section.splitlines():
            if line.strip() and not line.strip().startswith('* '):
                updated_section.append(f"* {line.strip()}")
            else:
                updated_section.append(line)
        updated_section = '\n'.join(updated_section)
        updated_content = updated_content.replace(section, updated_section)

    return updated_content

def process_markdown_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = ensure_bullets_in_section(content, "Supports:")
                new_content = ensure_bullets_in_section(new_content, "Supported By:")

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    directory_to_scan = "./content/patterns/"  # Change this to your directory path
    process_markdown_files(directory_to_scan)
