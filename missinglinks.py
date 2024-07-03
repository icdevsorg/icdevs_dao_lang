import os
import re
from bs4 import BeautifulSoup

def find_local_files_in_md(file_path):
    missing_files = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Find markdown links and images
        md_links = re.findall(r'!\[.*?\]\((.*?)\)', content) + re.findall(r'\[.*?\]\((.*?)\)', content)
        for link in md_links:
            if not link.startswith(('http://', 'https://')):
                if not check_file_exists(os.path.dirname(file_path), link):
                    missing_files.append(link)
                    
    return missing_files

def find_local_files_in_html(file_path):
    missing_files = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find HTML links and images
        html_links = [img['src'] for img in soup.find_all('img', src=True)] + [a['href'] for a in soup.find_all('a', href=True)]
        for link in html_links:
            if not link.startswith(('http://', 'https://')):
                if not check_file_exists(os.path.dirname(file_path), link):
                    missing_files.append(link)
                    
    return missing_files

def check_file_exists(directory, file_link):
    file_name, file_ext = os.path.splitext(file_link)
    for ext in ['.md', '.html', file_ext]:
        if os.path.exists(os.path.join(directory, file_name + ext)):
            return True
    return False

def scan_directory(directory):
    missing_files_report = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_path = os.path.join(root, file)
                missing_files = find_local_files_in_md(md_path)
                if missing_files:
                    missing_files_report[md_path] = missing_files
            elif file.endswith('.html'):
                html_path = os.path.join(root, file)
                missing_files = find_local_files_in_html(html_path)
                if missing_files:
                    missing_files_report[html_path] = missing_files
                    
    return missing_files_report

def print_missing_files_report(report):
    if report:
        for file_path, missing_files in report.items():
            print(f"Missing files in {file_path}:")
            for missing_file in missing_files:
                print(f"  - {missing_file}")
    else:
        print("No missing files found.")

if __name__ == "__main__":
    directory_to_scan = "./content/"
    missing_files_report = scan_directory(directory_to_scan)
    print_missing_files_report(missing_files_report)
