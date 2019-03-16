from denite.kind.base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'gitto'
        self.default_action = 'run'

    def action_run(self, context):
        target = context['targets'][0]
        if target['action__type'] == 'func':
            self.vim.call(target['action__func'], *target['action__args'])
            context['sources_queue'].append([{'name': 'gitto', 'args': []}])
        elif target['action__type'] == 'source':
            context['sources_queue'].append(target['action__source'])

