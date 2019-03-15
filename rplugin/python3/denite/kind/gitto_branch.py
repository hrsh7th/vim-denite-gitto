from denite.kind.base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'gitto/branch'
        self.default_action = 'checkout'
        self.redraw_actions = []
        self.redraw_actions += ['checkout']
        self.redraw_actions += ['rename']
        self.redraw_actions += ['push']
        self.redraw_actions += ['pull']
        self.redraw_actions += ['merge']
        self.redraw_actions += ['merge_no_ff']
        self.redraw_actions += ['rebase']
        self.redraw_actions += ['new']
        self.persist_actions = self.redraw_actions

    def action_checkout(self, context):
        branch = context['targets'][0]['action__branch']
        self.vim.call('gitto#run', 'branch#checkout', branch['name'])

    def action_rename(self, context):
        branch = context['targets'][0]['action__branch']
        new_name = self.vim.call('input', 'rename branch {} -> '.format(branch['name']))
        self.vim.call('gitto#run', 'branch#rename', branch['name'], new_name)

    def action_new(self, context):
        name = self.vim.call('input', 'create branch: ')
        self.vim.call('gitto#run', 'branch#new', name)

    def action_merge(self, context):
        branch = context['targets'][0]['action__branch']
        self.vim.call('gitto#run', 'branch#merge', branch['name'])

    def action_merge_no_ff(self, context):
        branch = context['targets'][0]['action__branch']
        self.vim.call('gitto#run', 'branch#merge', branch['name'], {'--no-ff': True})

    def action_rebase(self, context):
        branch = context['targets'][0]['action__branch']
        self.vim.call('gitto#run', 'branch#rebase', branch['name'])

    def action_push(self, context):
        branch = context['targets'][0]['action__branch']
        self.vim.call('gitto#run', 'branch#push', branch)

    def action_pull(self, context):
        branch = context['targets'][0]['action__branch']
        self.vim.call('gitto#run', 'branch#pull', branch)
