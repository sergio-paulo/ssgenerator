#!/usr/bin/env python3
"""
main
"""

from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

def main():
    """
    Main function
    """
    text_node = TextNode("Hello, World!", TextType.LINK, "https://www.boot.dev")
    print(text_node)
    
    html_node = HTMLNode("a", "backend", None, {"href": "www.boot.dev"})
    print(html_node)
    print(f"Node props_to_html: {html_node.props_to_html()}")
    
    '''
    node = ParentNode(
        "html",
        [
            ParentNode(
                "head",
                [
                    LeafNode("title", "Why Frontend Development Sucks")
                ]),
            ParentNode(
                "body",
                [
                    LeafNode("h1", "Front-end Development is the Worst"),
                    ParentNode(
                        "p",
                        [
                            LeafNode(
                                None,
                                "Look, front-end development is for script kiddies and soydevs who can't"
                            ),
                            LeafNode(
                                None,
                                "handle the real programming. I mean, it's just a bunch of divs and spans,"
                            ),
                            LeafNode(
                                None,
                                "right? And css??? It's like, \"Oh, I want this to be red, but not thaaaaat"
                            ),
                            LeafNode(
                                None,
                                "red.\" What a joke."
                            ),
                        ]
                    ),
                    ParentNode(
                        "p",
                        [
                            LeafNode(
                                None,
                                "Real programmers code, not silly markup languages. They code on Arch"
                            ),
                            LeafNode(
                                None,
                                "Linux, not macOS, and certainly not Windows. They use Vim, not VS Code."
                            ),
                            LeafNode(
                                None,
                                "They use C, not HTML. Come to the"
                            ),
                            LeafNode(
                                "a",
                                "backend",
                                {"href": "https://www.boot.dev"}
                            ),
                            LeafNode(
                                None,
                                ", where the real programming happens."
                            )
                        ]
                    )
                ]
            )
        ] 
    )
    print(node.to_html())
    '''
    

    print("\n")
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    print("[")
    for node in nodes:
        print(f"\t{node}")
    print("]")
    
    print("\n")
    node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and an image ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
    new_nodes = split_nodes_link([node])
    new_nodes = split_nodes_image(new_nodes)
    for node in new_nodes:
        print(node)

    
main()
