#!/usr/bin/env python3
"""
main
"""

from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from block_markdown import markdown_to_blocks

def main():
    """
    Main function
    """
    markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
    print(markdown_to_blocks(markdown))
        
main()
