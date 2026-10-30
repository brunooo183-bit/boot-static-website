class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if not self.props:
            return ""

        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'

        return result

    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a value")
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value

        props_str = ""
        for key, val in self.props.items():
            props_str += f' {key}="{val}"'

        # If there's no value (empty string), it's a self-closing tag
        if self.value == "":
            return f"<{self.tag}{props_str}>"
        else:
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag!r}, value={self.value!r}, props={self.props!r})"           