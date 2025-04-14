def markdown_to_blocks(markdown):
    blocks_list = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block != "":
            blocks_list.append(block.strip())
    return blocks_list
 