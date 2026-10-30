import unittest
from htmlnode import HTMLNode , LeafNode , ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            value=None,
            children=[],
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode(
            tag="p",
            value="Hello",
            children=[],
            props={}
        )
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode(
            tag="p",
            value="Hello",
            children=[],
            props=None
        )
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(
            tag="p",
            value="Hello",
            children=[],
            props={"class": "text"}
        )
        expected = "HTMLNode(tag='p', value='Hello', children=[], props={'class': 'text'})"
        self.assertEqual(repr(node), expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_empty_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("img", "", {"src": "image.jpg", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="image.jpg" alt="An image">')

    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "value")
        self.assertEqual(node.to_html(), "value") 

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

    def test_to_html_multiple_children(self):
        child1 = LeafNode("p", "text1")
        child2 = LeafNode("p", "text2")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><p>text1</p><p>text2</p></div>")

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "text")])

    def test_to_html_nested_parent_nodes(self):
        inner_child = LeafNode("span", "inner")
        outer_child = ParentNode("div", [inner_child])
        parent_node = ParentNode("body", [outer_child])
        self.assertEqual(
            parent_node.to_html(),
            "<body><div><span>inner</span></div></body>",
        )

    def test_to_html_parent_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')

    def test_to_html_complex_nesting(self):
        grandchild1 = LeafNode("b", "bold")
        grandchild2 = LeafNode("i", "italic")
        child1 = ParentNode("p", [grandchild1])
        child2 = ParentNode("p", [grandchild2])
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p><b>bold</b></p><p><i>italic</i></p></div>",
        )       

if __name__ == "__main__":
    unittest.main()