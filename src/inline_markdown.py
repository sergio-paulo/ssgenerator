import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node_list.append(node)
        else:
            split_nodes = []
            splited_text = node.text.split(delimiter)
            if len(splited_text) % 2 == 0:
                raise ValueError(f"Invalid text format: {node.text}")
            else:
                for i in range(len(splited_text)):
                    if splited_text[i] == "":
                        continue
                    if i % 2 == 0:
                        split_nodes.append(TextNode(splited_text[i], TextType.TEXT))
                    else:
                        split_nodes.append(TextNode(splited_text[i], text_type))
                new_node_list.extend(split_nodes)
    return new_node_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node_list.append(node)
            continue
        else:
            text = node.text
            images = extract_markdown_images(node.text)
            if not images:
                new_node_list.append(node)
                continue
            for (image_alt, image_link) in images:
                sections = text.split(f"![{image_alt}]({image_link})", maxsplit=1)
                if len(sections) != 2:
                    raise ValueError(f"Invalid markdown format, image section not closed")
                if sections[0] != "":
                    new_node_list.append(TextNode(sections[0], TextType.TEXT))
                new_node_list.append(TextNode(image_alt, TextType.IMAGE, image_link))
                text = sections[1]
        if text != "":
            new_node_list.append(TextNode(text, TextType.TEXT))
    return new_node_list

def split_nodes_link(old_nodes):
    new_node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node_list.append(node)
            continue
        else:
            text = node.text
            links = extract_markdown_links(node.text)
            if len(links) == 0:
                new_node_list.append(node)
                continue
            for (link_name, link_url) in links:
                sections = text.split(f"[{link_name}]({link_url})", maxsplit=1)
                if len(sections) != 2:
                    raise ValueError(f"Invalid markdown format, link section not closed")
                if sections[0] != "":
                    new_node_list.append(TextNode(sections[0], TextType.TEXT))
                new_node_list.append(TextNode(link_name, TextType.LINK, link_url))
                text = sections[1]
        if text != "":
            new_node_list.append(TextNode(text, TextType.TEXT))
    return new_node_list

def text_to_textnodes(text):
    types = [TextType.BOLD, TextType.ITALIC, TextType.CODE, TextType.LINK, TextType.IMAGE]
    nodes = [TextNode(text, TextType.TEXT)]
    for text_type in types:
        match text_type:
            case TextType.BOLD:
                nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
            case TextType.ITALIC:
                nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
            case TextType.CODE:
                nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
            case TextType.LINK:
                nodes = split_nodes_link(nodes)
            case TextType.IMAGE:
                nodes = split_nodes_image(nodes)
    return nodes