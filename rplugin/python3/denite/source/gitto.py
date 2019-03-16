from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto'
        self.kind = 'gitto'
        self.vars = {}
        self.label_length = 12

    def gather_candidates(self, context):
        branch = self.vim.call('gitto#run', 'branch#current')
        candidates = []
        self._status(context, candidates)
        self._branch(context, candidates)
        self._log(context, candidates)
        self._fetch(context, candidates)
        self._push(context, candidates, branch)
        self._push_force(context, candidates, branch)
        self._pull(context, candidates, branch)
        self._pull_rebase(context, candidates, branch)
        for candidate in candidates:
            candidate.update({
                'word': '{:{label}} | {}'.format(*candidate['word'], label=self.label_length),
                'abbr': '{:{label}} | {}'.format(*candidate['word'], label=self.label_length)
            })
        return candidates

    def _push(self, context, candidates, branch):
        if branch and branch['ahead'] > 0:
            candidates.append({
                'word': ['push', 'target is `{}/{}`, {} commits'.format(branch['remote'], branch['name'], branch['ahead'])],
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#push']
            })

    def _push_force(self, context, candidates, branch):
        if branch and branch['ahead'] > 0:
            candidates.append({
                'word': ['push force', 'target is `{}/{}`, {} commits'.format(branch['remote'], branch['name'], branch['ahead'])],
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#push', {'--force': True}]
            })

    def _pull(self, context, candidates, branch):
        if branch and branch['behind'] > 0:
            candidates.append({
                'word': ['pull', 'target is `{}`'.format(branch['upstream'])],
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#pull']
            })

    def _pull_rebase(self, context, candidates, branch):
        if branch and branch['behind'] > 0:
            candidates.append({
                'word': ['pull --rebase', 'target is `{}`'.format(branch['upstream'])],
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#pull', {'--rebase': True}]
            })

    def _fetch(self, context, candidates):
        candidates.append({
            'word': ['fetch', ''],
            'action__type': 'func',
            'action__func': 'gitto#run',
            'action__args': ['repo#fetch', {'--all': True, '--prune': True}]
        })

    def _status(self, context, candidates):
        candidates.append({
            'word': ['status', ''],
            'action__type': 'source',
            'action__source': [{'name': 'gitto/status', 'args': []}]
        })

    def _branch(self, context, candidates):
        candidates.append({
            'word': ['branch', '-a'],
            'action__type': 'source',
            'action__source': [{'name': 'gitto/branch', 'args': ['-a']}]
        })

    def _log(self, context, candidates):
        candidates.append({
            'word': ['log', ''],
            'action__type': 'source',
            'action__source': [{'name': 'gitto/log', 'args': []}]
        })

