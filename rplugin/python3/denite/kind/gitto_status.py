from denite.kind.file import Kind as File

class Kind(File):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'gitto/status'
        self.default_action = 'diff'
        self.redraw_actions = []
        self.redraw_actions += ['reset']
        self.redraw_actions += ['rm']
        self.redraw_actions += ['add']
        self.redraw_actions += ['checkout']
        self.redraw_actions += ['diff']
        self.persist_actions = self.redraw_actions

    def action_reset(self, context):
        self._per_status('status#reset', context)

    def action_rm(self, context):
        self._per_status('status#rm', context)

    def action_add(self, context):
        self._per_status('status#add', context)

    def action_checkout(self, context):
        self._per_status('status#checkout', context)

    def action_commit(self, context):
        paths = [candidate['action__path'] for candidate in context['targets']]
        self.vim.call('denite_gitto#commit', paths)

    def action_diff(self, context):
        paths = [candidate['action__path'] for candidate in context['targets']]
        for path in paths:
            self.vim.call('denite_gitto#diff_file_with_hash', path, {'hash': 'HEAD', 'path': path})

    def _per_status(self, action, context):
        paths = [candidate['action__path'] for candidate in context['targets']]
        self.vim.call('denite_gitto#run', action, paths)

