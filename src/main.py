#!/usr/bin/env python3
"""
main
"""
from copystatic import copy_tree
from gencontent import generate_pages_recursive
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
    
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)   
    
main()

