class Row(object):
    def __init__(self, title='test', children=None, **defaults):
        self.title = title
        self.children = children or []
        self.defaults = defaults

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
        base = {}
        base.update(self.defaults)
        args = reduce(
            lambda a, d: a.update(d.as_dict()) or a,
            params,
            base
        )
        return '{}({})'.format(
            self.title,
            ', '.join(['%s=%s' % (k, v) for (k, v) in args.iteritems()]),
        )

    def render(self, columns):
        return {
            'title': self.title,
            'children': self.render_children(columns),
            'data': self.render_data(columns),
        }
