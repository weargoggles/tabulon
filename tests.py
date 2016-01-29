import json
import unittest

from tabulon import Column, Constraint, Row


class Colour(Constraint):
    def __init__(self, colour):
        self.colour = colour

    def render_key(self):
        return self.colour


class Foo(Constraint):

    def render_key(self):
        return 'foo'


class TestTable(unittest.TestCase):
    def test_table(self):
        child_row = Row(title='test child')
        row = Row(title='test row', children=[child_row])

        red_child = Column(Colour('red'))
        blue_child = Column(Colour('blue'))
        child_columns = [red_child, blue_child]
        column = Column(Foo(), children=child_columns, )

        result = row.render([column])
        self.assertEqual(result, {
            'data': [{
                'key': 'foo',
                'sub_columns': [
                    {
                        'key': 'red', 'value': 'f(foo, red)',
                    },
                    {
                        'key': 'blue', 'value': 'f(foo, blue)',
                    },
                ],
            }],
            'children': [],
            'title': 'test row',
        })
