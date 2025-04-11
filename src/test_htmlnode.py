import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        self.assertEqual(repr(node), "HTMLNode(p, just som text, children=None, None)")
        
    def test_repr_props(self):
        node = HTMLNode(
            "a",
            "backend",
            None,
            {"href": "www.boot.dev", "class": "btn btn-primary"}
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(a, backend, children=None, {'href': 'www.boot.dev', 'class': 'btn btn-primary'})")
        
    def test_props_to_html(self):
        node = HTMLNode("a", "backend", None, {"href": "www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="www.boot.dev"')

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
            
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_parent_to_html(self):
            node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            self.assertEqual(
                node.to_html(),
                "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            )
            
    def test_parent_to_html2(self):
            node = ParentNode(
                "html",
                [
                    ParentNode(
                        "head",
                        [
                            LeafNode("title", "Why Frontend Development Sucks")
                        ]),
                    ParentNode(
                        "body",
                        [
                            LeafNode("h1", "Front-end Development is the Worst"),
                            ParentNode(
                                "p",
                                [
                                    LeafNode(
                                        None,
                                        "Look, front-end development is for script kiddies and soydevs who can't "
                                    ),
                                    LeafNode(
                                        None,
                                        "handle the real programming. I mean, it's just a bunch of divs and spans, "
                                    ),
                                    LeafNode(
                                        None,
                                        'right? And css??? It\'s like, "Oh, I want this to be red, but not thaaaaat '
                                    ),
                                    LeafNode(
                                        None,
                                        'red." What a joke.'
                                    ),
                                ]
                            ),
                            ParentNode(
                                "p",
                                [
                                    LeafNode(
                                        None,
                                        "Real programmers code, not silly markup languages. They code on Arch "
                                    ),
                                    LeafNode(
                                        None,
                                        "Linux, not macOS, and certainly not Windows. They use Vim, not VS Code. "
                                    ),
                                    LeafNode(
                                        None,
                                        "They use C, not HTML. Come to the "
                                    ),
                                    LeafNode(
                                        "a",
                                        "backend",
                                        {"href": "https://www.boot.dev"}
                                    ),
                                    LeafNode(
                                        None,
                                        ", where the real programming happens."
                                    )
                                ]
                            )
                        ]
                    )
                ] 
            )
            self.assertEqual(
                node.to_html(),
                "<html><head><title>Why Frontend Development Sucks</title></head><body><h1>Front-end Development is the Worst</h1><p>Look, front-end development is for script kiddies and soydevs who can't handle the real programming. I mean, it's just a bunch of divs and spans, right? And css??? It's like, \"Oh, I want this to be red, but not thaaaaat red.\" What a joke.</p><p>Real programmers code, not silly markup languages. They code on Arch Linux, not macOS, and certainly not Windows. They use Vim, not VS Code. They use C, not HTML. Come to the <a href=\"https://www.boot.dev\">backend</a>, where the real programming happens.</p></body></html>"
            )
            
if __name__ == "__main__":
    unittest.main()