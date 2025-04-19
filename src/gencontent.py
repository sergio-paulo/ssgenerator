import os
from md_html import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Generate all the pages in a directory
    """
    for entry in os.listdir(dir_path_content):
            src_path = os.path.join(dir_path_content, entry)
            dst_path = os.path.join(dest_dir_path, entry)
            if os.path.isdir(src_path):
                if not os.path.exists(dst_path):
                    os.mkdir(dst_path)
                generate_pages_recursive(src_path, template_path, dst_path)
            else:
                dst_path = dst_path.replace(".md", ".html")
                generate_page(src_path, template_path, dst_path)
    

def generate_page(from_path, template_path, dest_path):
    """
    Generate a page from a template
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    
    # Read the markdown source file
    with open(from_path, "r") as file:
        src = file.read()
    
    # Read the hml template file
    with open(template_path, "r") as file:
        template = file.read()
        
    # convert the markdown to html
    src_to_node = markdown_to_html_node(src)
    node_to_html = src_to_node.to_html()
        
    # extract the title from the markdown
    title = extract_title(src)
    
    # replace the placeholders in the template
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", node_to_html)
    
    # write the html to the destination file
    if not os.path.exists(os.path.dirname(dest_path)):
        shutil.os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as file:
        file.write(template)
        
def extract_title(markdown):
    """
    Extract the title from the markdown file
    """
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found in markdown file")

'''
    def list_files_recursive(path):
        items = []
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            items.append(full_path)
            if os.path.isdir(full_path):
                items.extend(list_files_recursive(full_path))
        return items
    
    files = list_files_recursive("./static/")
    print(f"files in ./static:\n{files}")
'''