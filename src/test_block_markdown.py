import unittest
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type

class TestUtilities(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
        
    def test_markdown_to_blocks_more_newlinew(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
""" 
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here"
            ])
    
    def test_markdown_to_blocks_no_newline(self):
        md = "This is **bolded** paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is **bolded** paragraph"])
    
    def test_markdown_to_blocks_with_whitespaces(self):
        md = """
    This is **bolded** paragraph

     This is another paragraph with _italic_ text and `code` here
""" 
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here"
            ])
        
    def test_block_to_block_type_heading(self):
        md = "# This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)
    
    def test_block_to_block_type_heading_3(self):
        md = "### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_block_to_block_type_heading_6(self):
        md = "###### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_block_to_block_type_code(self):
        md = "```\nThis is a code block\nwith multiline\n```"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_block_type_quote(self):
        md = ">This is the first line of a quote\n>This is the second line of a quote"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)
        
    def test_block_to_block_type_unordered_list(self):
        md = "- This is the first line of a list\n- This is the second line of a list"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ULIST)
    
    def test_block_to_block_type_ordered_list(self):
        md = "1. This is the first line of a list\n2. This is the second line of a list\n3. This is the third line of a list"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.OLIST)
    
if __name__ == "__main__":
    unittest.main()