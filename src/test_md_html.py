import unittest
from md_html import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    """
    Test class for markdown_to_html_node function.
    """

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
        
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        )
        
    def test_heading(self):
        md = """
# This is a heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1></div>"
        )
        
    def test_heading_3(self):
        md = """
### This is a heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a heading</h3></div>"
        )
        
    def test_quote(self):
        md = """
> This is a quote
> with a new line
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with a new line</blockquote></div>"
        )
        
    def test_quote_with_empty_line(self):
        md = """
> This is a quote
> 
> with a new line
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with a new line</blockquote></div>"
        )
        
    def test_unordered_list(self):
        md = """
- This is a list item
- This is another list item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list item</li><li>This is another list item</li></ul></div>"
        )
        
    def test_ordered_list(self):
        md = """
1. This is a list item
2. This is another list item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is a list item</li><li>This is another list item</li></ol></div>"
        )
        
if __name__ == "__main__":
    unittest.main()