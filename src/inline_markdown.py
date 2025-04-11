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