from block_markdown import BlockType, markdown_to_blocks, block_to_block_type
from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes

'''
have to convert markdown blocks to textodes first

have to create text_to_children(text) function

each type of markdown block goes on a ParenNode with the respective tag:
- Paragraph -> <p>
- Heading -> <h1>, <h2>, <h3>, <h4>, <h5>, <h6>
- Code -> <pre><code>
- Quote -> <blockquote>
- Unordered list -> <ul><li>
- Ordered list -> <ol><li>

Then inside each block the text is processed for the inline markdown
- Bold -> <b>
- Italic -> <i>
- Code -> <code>
- Image -> <img src="url" alt="text" />
- Link -> <a href="url">text</a>
'''



def markdown_to_html_node(md):
    div_nodes = []
    blocks = markdown_to_blocks(md)
    for block in blocks:
        if len(block) == 0:
            continue
        else:
            html_node = block_to_html_node(block)
            div_nodes.append(html_node)
    return ParentNode("div", div_nodes, None)

def block_to_html_node(block):    
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                return paragraph_to_html_node(block)
            case BlockType.HEADING:
                return heading_to_html_node(block)
            case BlockType.CODE:
                return code_to_html_node(block)
            case BlockType.QUOTE:
                return quote_to_html_node(block)
            case BlockType.ULIST:
                return ulist_to_html_node(block)
            case BlockType.OLIST:
                return olist_to_html_node(block)
            case _:
                raise ValueError(f"invalid block type")


def text_to_children(text):
    # Return list of children LeafNodes
    nodes = text_to_textnodes(text)
    children = list(map(lambda x: x.text_node_to_html_node(), nodes))
    return children


def paragraph_to_html_node(block):
    # Handle paragraph
    # Text block with possible inline markdown
    paragraph = " ".join(block.strip().split("\n"))
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):    
    # Handle heading
    # Heading block with possible inline markdown
    # Must get number of #s
    (head, text) = block.split(" ", 1)
    level = len(head)
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

    
def quote_to_html_node(block):
    # Handle quote
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError(f"invalid quote block")
        else:
            text = line.lstrip(">").strip()
            if text != "":
                new_lines.append(text)
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

            
def code_to_html_node(block):
    # Handle code
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError(f"invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = raw_text_node.text_node_to_html_node()
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

            
def ulist_to_html_node(block):
    # Handle unordered list
    parent_li = []
    lines = block.split("\n")
    for line in lines:
        parent_li.append(ParentNode("li", text_to_children(line[2:])))
    return ParentNode("ul", parent_li)

 
def olist_to_html_node(block):
    # Handle ordered list
    parent_li = []
    lines = block.split("\n")
    for line in lines:
        start = line.find(". ")
        parent_li.append(ParentNode("li", text_to_children(line[start + 2:])))
    return ParentNode("ol", parent_li)
    