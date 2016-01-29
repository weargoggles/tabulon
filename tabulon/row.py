class Row(object):
    def __init__(self, title='test', children=None):
        self.title = title
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)

    def render_children(self, columns):
        return [
            child.render(columns) for child in self.children
        ]

    def render_data(self, columns):
        return [
            column.render_cell(self) for column in columns
        ]

    def get_value(self, *params):
        return 'f({})'.format(', '.join(p.render_key() for p in params))

    def render(self, columns):
        return {
            'title': self.title,
            'children': self.render_children(columns),
            'data': self.render_data(columns),
        }
