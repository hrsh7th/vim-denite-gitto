from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto/status'
        self.kind = 'gitto/status'
        self.vars = {}

    def gather_candidates(self, context):
        statuses = self.vim.call('gitto#run', 'status#get')
        return [{
            'word': '{:<4} | {}'.format(status['status'], status['path']),
            'abbr': '{:<4} | {}'.format(status['status'], status['path']),
            'action__status': status,
            'action__path': status['path']
        } for status in statuses]
