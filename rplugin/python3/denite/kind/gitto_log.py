from denite.kind.base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'gitto/log'
        self.redraw_actions = []
        self.redraw_actions += ['reset']
        self.redraw_actions += ['reset_soft']
        self.redraw_actions += ['reset_hard']
        self.persist_actions = self.redraw_actions

    def action_reset(self, context):
        self._reset(context, {})

    def action_reset_soft(self, context):
        self._reset(context, {'--soft': True})

    def action_reset_hard(self, context):
        self._reset(context, {'--hard': True})

    def _reset(self, context, opts):
        commit_hash = context['targets'][0]['action__log']['commit_hash']
        self.vim.call('gitto#run', 'log#reset', commit_hash, opts)
