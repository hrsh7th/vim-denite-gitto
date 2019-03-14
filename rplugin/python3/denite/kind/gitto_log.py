from denite.kind.base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'gitto/log'
        self.default_action = 'changes'
        self.redraw_actions = []
        self.redraw_actions += ['reset']
        self.redraw_actions += ['reset_soft']
        self.redraw_actions += ['reset_hard']
        self.persist_actions = self.redraw_actions

    def action_changes(self, context):
        log = context['targets'][0]['action__log']

        if not len(log['parent_hashes']):
            self.vim.command('echomsg "{}"'.format('Selected log has\'nt parent.'))
            return

        context['sources_queue'].append([
            {'name': 'gitto/changes', 'args': [log['parent_hashes'][0], log['commit_hash']]}
        ])

    def action_changes_to_head(self, context):
        log = context['targets'][0]['action__log']
        context['sources_queue'].append([
            {'name': 'gitto/changes', 'args': [log['commit_hash'], 'HEAD']}
        ])

    def action_reset(self, context):
        self._reset(context, {})

    def action_reset_soft(self, context):
        self._reset(context, {'--soft': True})

    def action_reset_hard(self, context):
        self._reset(context, {'--hard': True})

    def _reset(self, context, opts):
        commit_hash = context['targets'][0]['action__log']['commit_hash']
        self.vim.call('gitto#run', 'log#reset', commit_hash, opts)
