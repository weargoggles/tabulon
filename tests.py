import unittest

from tabulon import Column, Constraint, Row


class Colour(Constraint):
    def __init__(self, colour):
        self.colour = colour

    def render_key(self):
        return self.colour

    def as_dict(self):
        return {'colour': self.colour}


class Foo(Constraint):

    def render_key(self):
        return 'foo'

    def as_dict(self):
        return {'foo': 'foo'}


class TestTable(unittest.TestCase):
    def test_table(self):
        child_row = Row(title='thingamajig', on=True)
        row = Row(title='widget', children=[child_row], cats='yes')

        red_child = Column(Colour('red'))
        blue_child = Column(Colour('blue'))
        child_columns = [red_child, blue_child]
        column = Column(Foo(), children=child_columns, )

        result = row.render([column])
        assert result == {
            'data': [{
                'key': 'foo',
                'sub_columns': [
                    {
                        'key': 'red', 'value': 'widget(colour=red, cats=yes, foo=foo)',
                    },
                    {
                        'key': 'blue', 'value': 'widget(colour=blue, cats=yes, foo=foo)',
                    },
                ],
            }],
            'children': [{
                'children': [],
                'data': [{
                    'key': 'foo',
                    'sub_columns': [
                        {
                            'key': 'red', 'value': 'thingamajig(on=True, colour=red, foo=foo)',
                        },
                        {
                            'key': 'blue', 'value': 'thingamajig(on=True, colour=blue, foo=foo)',
                        },
                    ],
                }],
                'title': 'thingamajig',
            }],
            'title': 'widget',
        }
