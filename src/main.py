#!/usr/bin/env python3
"""
main
"""

from textnode import TextNode, TextType

def main():
    """
    Main function
    """
    text_node = TextNode("Hello, World!", TextType.LINK, "https://www.boot.dev")
    print(text_node)
    
main()
