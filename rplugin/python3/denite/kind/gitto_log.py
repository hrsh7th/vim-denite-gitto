from denite.kind.base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'gitto/log'
        self.default_action = 'changes'
        self.redraw_actions = []
        self.redraw_actions += ['yank_revision']
        self.redraw_actions += ['reset']
        self.redraw_actions += ['reset_mixed']
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

    def action_changes_head(self, context):
        log = context['targets'][0]['action__log']
        context['sources_queue'].append([
            {'name': 'gitto/changes', 'args': [log['commit_hash'], 'HEAD']}
        ])

    def action_yank_revision(self, context):
        _yank(self.vim, context['targets'][0]['action__log']['commit_hash'])

    def action_reset(self, context):
        choise = self.vim.call('input', 'mixed/soft/hard: ')
        if choise  in ['mixed', 'soft', 'hard']:
            if choise == 'mixed':
                self._reset(context, {'--mixed': True})
            elif choise == 'soft':
                self._reset(context, {'--soft': True})
            elif choise == 'hard':
                self._reset(context, {'--hard': True})
            return

    def action_reset_mixed(self, context):
        self._reset(context, {'--mixed': True})

    def action_reset_soft(self, context):
        self._reset(context, {'--soft': True})

    def action_reset_hard(self, context):
        self._reset(context, {'--hard': True})

    def _reset(self, context, opts):
        commit_hash = context['targets'][0]['action__log']['commit_hash']
        self.vim.call('denite_gitto#run', 'log#reset', commit_hash, opts)

def _yank(vim, word):
    vim.call('setreg', '"', word, 'v')
    if vim.call('has', 'clipboard'):
        vim.call('setreg', vim.eval('v:register'), word, 'v')
