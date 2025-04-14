import re
from enum import Enum

class BlockType(Enum):
    """
    Enum for block types.
    """
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks_list = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block != "":
            blocks_list.append(block.strip())
    return blocks_list

def block_to_block_type(md_block):
    if re.findall(r"^(#{1,6})(?!#)\s", md_block) != []:
        return BlockType.HEADING
    elif re.findall(r"^'''[\s\S]*'''", md_block) != []:
        return BlockType.CODE
    elif re.findall(r">\s(.*?)\n", md_block) != []:
        return BlockType.QUOTE
    elif re.findall(r"-\s(.*?)\n", md_block) != []:
        return BlockType.ULIST
    elif re.findall(r"\d*.\s(.*?)\n", md_block) != []:
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH