#!/usr/bin/env python3
"""
main
"""

from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    """
    Main function
    """
    text_node = TextNode("Hello, World!", TextType.LINK, "https://www.boot.dev")
    print(text_node)
    
    html_node = HTMLNode("a", "backend", None, {"href": "www.boot.dev"})
    print(html_node)
    print(f"Node props_to_html: {html_node.props_to_html()}")
    
main()
