class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children={self.children}, {self.props})"
    
    def __eq__(self, value):
        return self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props
    
    def to_html(self):
        """
        Convert the HTML node to an HTML string.
        """
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        """
        Convert the props to an HTML string.
        """
        if not self.props:
            return ""
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result


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
    

class ParentNode(HTMLNode):
    """
    A class representing a parent node in an HTML tree.
    """
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        """
        Convert the parent node to an HTML string.
        """
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        
        if not self.children:
            raise ValueError("Parent node must have children")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children={self.children}, {self.props})"