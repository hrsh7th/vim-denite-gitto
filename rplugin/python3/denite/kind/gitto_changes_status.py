from denite.kind.base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'gitto/changes_status'
        self.default_action = 'diff'
        self.redraw_actions = ['diff']
        self.persist_actions = self.redraw_actions

    def action_diff(self, context):
        from_hash = context['targets'][0]['action__changes']['from']
        to_hash = context['targets'][0]['action__changes']['to']

        statuses = [candidate['action__status'] for candidate in context['targets']]
        for status in statuses:
            if status['status'] == 'R':
                self.vim.call('denite_gitto#diff_hash_with_hash', {'hash': to_hash, 'path': status['path']}, {'hash': from_hash, 'path': status['path_before_rename']})
            else:
                self.vim.call('denite_gitto#diff_hash_with_hash', {'hash': to_hash, 'path': status['path']}, {'hash': from_hash, 'path': status['path']})

