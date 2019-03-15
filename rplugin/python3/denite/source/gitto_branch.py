from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto/branch'
        self.kind = 'gitto/branch'
        self.vars = {}

    def gather_candidates(self, context):
        branches = self.vim.call('gitto#run', 'branch#get', self._option(context))
        return [{
            'word': branch['raw'],
            'abbr': branch['raw'],
            'action__branch': branch,
        } for branch in branches]

    def _option(self, context):
        option = {}
        for arg in context['args']:
            parts = arg.split('=')
            if len(parts) == 1:
                option[parts[0]] = True
            elif len(parts) == 2:
                option[parts[0]] = parts[1]
        return option

