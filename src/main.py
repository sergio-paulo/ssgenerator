#!/usr/bin/env python3
"""
main
"""
from md_html import markdown_to_html_node
import os
import shutil

def main():
    """
    Main function
    """
    
    def copy_tree(src, dst):
        """
        Copy a directory tree
        """
        if os.path.exists(dst):
            print(f"{dst} already exists, removing it")
            shutil.rmtree(dst)
        print(f"{dst} does not exist, creating it")
        os.mkdir(dst)
        
        for item in os.listdir(src):
            print(f"processing {item}")
            src_path = os.path.join(src, item)
            print(f"src_path: {src_path}")
            dst_path = os.path.join(dst, item)
            print(f"dst_path: {dst_path}")
            if os.path.isdir(src_path):
                print(f"copying directory {src_path} to {dst_path}")
                copy_tree(src_path, dst_path)
            else:
                print(f"copying file {src_path} to {dst_path}")
                shutil.copy(src_path, dst_path)
    
    copy_tree("./static", "./public")
    
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
