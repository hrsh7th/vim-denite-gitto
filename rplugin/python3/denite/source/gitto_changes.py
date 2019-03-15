from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto/changes'
        self.kind = 'gitto/changes_status'
        self.vars = {}

    def gather_candidates(self, context):
        changes = self.vim.call('gitto#run', 'changes#get', context['args'][0], context['args'][1])
        if not len(changes['statuses']):
            return []

        return [{
            'word': '{:>3} | {}'.format(status['status'], status['path']),
            'abbr': '{:>3} | {}'.format(status['status'], status['path']),
            'action__changes': changes,
            'action__status': status,
            'action__path': status['path']
        } for status in changes['statuses']]

