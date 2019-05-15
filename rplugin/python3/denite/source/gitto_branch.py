from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto/branch'
        self.kind = 'gitto/branch'
        self.vars = {}

    def gather_candidates(self, context):
        branches = self.vim.call('denite_gitto#run', 'branch#get', self._option(context))

        lengths = self._column_len(branches, [
            'refname',
            'remote',
            'upstream'
        ])

        return [{
            'word': '{:1} | {:{refname}} | {:{remote}} | {:{upstream}} | {}'.format(
                branch['HEAD'],
                branch['name'] if branch['local'] else branch['refname'],
                branch['remote'],
                branch['upstream'],
                branch['upstream_track'],
                refname=lengths['refname'],
                remote=lengths['remote'],
                upstream=lengths['upstream']
            ),
            'abbr': '{:1} | {:{refname}} | {:{remote}} | {:{upstream}} | {}'.format(
                branch['HEAD'],
                branch['name'] if branch['local'] else branch['refname'],
                branch['remote'],
                branch['upstream'],
                branch['upstream_track'],
                refname=lengths['refname'],
                remote=lengths['remote'],
                upstream=lengths['upstream']
            ),
            'action__branch': branch
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

    def _column_len(self, candidates, columns):
        lengths = {}
        for key in columns:
            lengths[key] = max([1] + [len(x[key]) for x in candidates])
        return lengths

