import unittest
from htmlnode import HTMLNode , LeafNode

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

if __name__ == "__main__":
    unittest.main()