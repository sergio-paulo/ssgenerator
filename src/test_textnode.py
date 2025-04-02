import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_eq2(self):
        node3 = TextNode("this is a link node", TextType.LINK, "https://www.boot.dev")
        node4 = TextNode("this is a link node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node3, node4)
        
    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    def test_uneq2(self):
        node3 = TextNode("this is a image node", TextType.IMAGE, "https://www.boot.dev")
        node4 = TextNode("this is a code node", TextType.CODE)
        self.assertNotEqual(node3, node4)
        
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        self.assertEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

if __name__ == "__main__":
    unittest.main()
