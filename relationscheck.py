import os
import re
import pygraphviz as pgv

def parse_patterns_dot(file_path):
    graph = pgv.AGraph(file_path)
    patterns = {}
    for edge in graph.edges():
        
        src, dest = edge
        if src not in patterns:
            patterns[src] = {'supports': set(), 'supported_by': set()}
        if dest not in patterns:
            patterns[dest] = {'supports': set(), 'supported_by': set()}
        patterns[src]['supports'].add(dest)
        patterns[dest]['supported_by'].add(src)
    print(f"patterns: {patterns}")
    return patterns

def parse_md_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regex to capture supports and supported by sections
    supports_section = re.findall(r'### Supports\s*:\s*([\s\S]*?)(?=\n###|\Z)', content)
    supported_by_section = re.findall(r'### Supported By\s*:\s*([\s\S]*?)(?=\n###|\Z)', content)

    # Extracting pattern names from the sections
    supports_patterns = set(re.findall(r'\[([^\]]+)\]\(./[^\)]+\)', supports_section[0])) if supports_section else set()
    supported_by_patterns = set(re.findall(r'\[([^\]]+)\]\(./[^\)]+\)', supported_by_section[0])) if supported_by_section else set()

    

    return supports_patterns, supported_by_patterns

def extract_pattern_name(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    match = re.search(r'^##\s+([A-Z]{2,4})\s*-\s*(.+)$', content, re.MULTILINE)
    if match:
        return match.group(2).strip()
    else:
        return os.path.basename(file_path).replace('.md', '')
    

def validate_patterns(directory, patterns_dot_path):
    patterns = parse_patterns_dot(patterns_dot_path)
    missing_links = {}

    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            pattern_name = extract_pattern_name(file_path)
            print(f"{pattern_name}:")
            file_path = os.path.join(directory, filename)
            supports, supported_by = parse_md_file(file_path)
            
            expected_supports = patterns.get(pattern_name, {}).get('supports', set())
            expected_supported_by = patterns.get(pattern_name, {}).get('supported_by', set())

            #print(f"expected supports: {expected_supports}:")
            #print(f" supports: {supports}:")
            #print(f"expected supports bu: {expected_supported_by}:")
            #print(f"supported by: {supported_by}:")
            
            missing_supports = expected_supports - supports
            missing_supported_by = expected_supported_by - supported_by
            
            if missing_supports or missing_supported_by:
                missing_links[filename] = []
                
                for pattern in missing_supports:
                    remotefilename = pattern.replace(' ', '_').replace('/', '_').replace('-', '_').lower()
                    print(f"Supports Missing: {filename}:")
                    print(f"* [{pattern}](./{remotefilename}.md)")
                    missing_links[filename].append(f"* [{pattern}](./{remotefilename}.md)")
                for pattern in missing_supported_by:
                    remotefilename = pattern.replace(' ', '_').replace('/', '_').replace('-', '_').lower()
                    print(f"Supported By Missing: {filename}:")
                    print(f"* [{pattern}](./{remotefilename}.md)")
                    missing_links[filename].append(f"* [{pattern}](./{remotefilename}.md)")
    
    return missing_links


if __name__ == "__main__":
    directory = './content/patterns/'
    patterns_dot_path = './patterns.dot'
    
    missing_links = validate_patterns(directory, patterns_dot_path)
    #print_missing_links(missing_links)
