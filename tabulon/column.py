import abc


class Constraint(object):
    class Meta(abc.ABCMeta):
        pass

    @abc.abstractmethod
    def render_key(self):
        raise NotImplementedError


class Column(object):
    def __init__(self, constraint, children=None):
        self.children = children or []
        assert isinstance(constraint, Constraint)
        self.constraint = constraint

    def render_cell(self, row, parent_constraints=None):
        constraints = (parent_constraints or []) + [self.constraint]
        if self.children:
            return {
                'key': self.constraint.render_key(),
                'sub_columns': [
                    child.render_cell(row, constraints)
                    for child in self.children
                ]
            }
        else:
            return {
                'key': self.constraint.render_key(),
                'value': row.get_value(*constraints)
            }
