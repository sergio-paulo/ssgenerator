import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestUtilities(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])
        
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])
        
    def test_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ])
        
    def test_bold_double(self):
        node = TextNode("This is text with a **bold** word and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and ", TextType.TEXT),
            TextNode("another", TextType.BOLD)
    ])
        
    def test_bold_multiword(self):
        node = TextNode("This is text with **bold words** and **another**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold words", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("another", TextType.BOLD)
    ])
        
    def test_bold_and_italic(self):
        node = TextNode("This is text with **bold words** and one _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold words", TextType.BOLD),
            TextNode(" and one ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
    ])
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_images_without_alttext(self):
        matches = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_images_with_url(self):
        matches = extract_markdown_images(
            "This is text with an ![image]()"
        )
        self.assertListEqual([("image", "")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)
        
    def test_extract_markdown_links_without_anchor(self):
        matches = extract_markdown_links(
            "This is text with a [](https://www.boot.dev)"
        )
        self.assertListEqual([("", "https://www.boot.dev")], matches)
        
    def test_extract_markdown_links_without_url(self):
        matches = extract_markdown_links(
            "This is text with a [link]()"
        )
        self.assertListEqual([("link", "")], matches)
        
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                )
            ],
            new_nodes
        )
        
    def test_split_link_and_image(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and an image ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(new_nodes)
        self.assertListEqual(new_nodes,
            [ 
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and an image ", TextType.TEXT),    
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ]
        )    
                    
    def test_text_to_textnodes_full(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev")
            ]
        )
    
    def test_text_to_textnodes_empty(self):
        text = ""
        new_nodes = text_to_textnodes(text)
        self.assertEqual(new_nodes, [])
        
    def test_text_to_textnodes_no_markdown(self):
        text = "This is a text without any markdown"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(new_nodes, [TextNode(text, TextType.TEXT)])
        
    def test_text_to_textnodes_with_code_and_bold(self):
        text = "This is a text with a `code block` and a **bold** word"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(new_nodes, [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ])
        
    def test_text_to_textnodes_with_link_and_code(self):
        text = "This is a text with a [link](https://www.boot.dev) and a `code block`"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(new_nodes, [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE)
        ])
        
    def test_text_to_textnodes_with_image_and_link(self):
        text = "This is a text with an image ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual(new_nodes, [
            TextNode("This is a text with an image ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.boot.dev")
        ])
    
        
if __name__ == "__main__":
    unittest.main()