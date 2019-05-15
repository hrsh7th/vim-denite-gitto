from denite.kind.base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'gitto/changes_status'
        self.default_action = 'diff'
        self.redraw_actions = ['diff']
        self.persist_actions = self.redraw_actions

    def action_diff(self, context):
        paths = [candidate['action__path'] for candidate in context['targets']]
        from_hash = context['targets'][0]['action__changes']['from']
        to_hash = context['targets'][0]['action__changes']['to']
        for path in paths:
            self.vim.call('denite_gitto#diff_hash_with_hash', {'hash': to_hash, 'path': path}, {'hash': from_hash, 'path': path})

