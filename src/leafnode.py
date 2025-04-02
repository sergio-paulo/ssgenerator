from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    """
    A class representing a leaf node in an HTML tree.
    """
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        """
        Convert the leaf node to an HTML string.
        """
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __eq__(self, value):
        return super().__eq__(value)
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    