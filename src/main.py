#!/usr/bin/env python3
"""
main
"""
from copystatic import copy_tree
from gencontent import generate_page
import os
import shutil

dir_path_static = "./static/"
dir_path_public = "./public/"
dir_path_content = "./content/"
template_path = "./template.html"

def main():
    """
    Main function
    """
    
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
            shutil.rmtree(dir_path_public)
    
    print("Copying static directory to public directory...")
    copy_tree(dir_path_static, dir_path_public)
    
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html")
    )    
    
main()

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
