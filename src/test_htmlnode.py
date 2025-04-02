import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "just som text")
        node2 = HTMLNode("p", "just som text")
        self.assertEqual(node, node2)
        
    def test_eq2(self):
        node = HTMLNode("a", "backend", None, {"href": "www.boot.dev"})
        node2 = HTMLNode("a", "backend", None, {"href": "www.boot.dev"})
        self.assertEqual(node, node2)
        
    def test_uneq(self):
        node = HTMLNode("p", "just som text")
        node2 = HTMLNode("p", "just some text2")
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = HTMLNode("p", "just som text")
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=just som text, children=None, props=None)")
        
    def test_props_to_html(self):
        node = HTMLNode("a", "backend", None, {"href": "www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="www.boot.dev"')
        