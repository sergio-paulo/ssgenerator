import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
            node = LeafNode("p", "Hello, world!")
            self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
            
    def test_leaf_to_html_a(self):
            node = LeafNode("a", "Click me!", {"href": "https://www.gogole.com"})
            self.assertEqual(node.to_html(), '<a href="https://www.gogole.com">Click me!</a>')
            
    def test_eq(self):
            node = LeafNode("p", "Hello, world!")
            node2 = LeafNode("p", "Hello, world!")
            self.assertEqual(node, node2)
            
    def test_repr(self):
            node = LeafNode("p", "Hello, world!")
            self.assertEqual(repr(node), "LeafNode(p, Hello, world!, None)")