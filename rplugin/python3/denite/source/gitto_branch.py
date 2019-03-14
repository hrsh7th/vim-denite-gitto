from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto/branch'
        self.kind = 'gitto/branch'
        self.vars = {}

    def gather_candidates(self, context):
        branches = self.vim.call('gitto#run', 'branch#get')
        return [{
            'word': branch['raw'],
            'abbr': branch['raw'],
            'action__branch': branch,
        } for branch in branches]



