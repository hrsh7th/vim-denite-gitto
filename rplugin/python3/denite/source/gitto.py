from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto'
        self.kind = 'gitto'
        self.vars = {}

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
        return [candidate for candidate in candidates if candidate]

    def _push(self, context, candidates, branch):
        if branch['ahead'] > 0:
            candidates.append({
                'word': 'push',
                'abbr': 'push',
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#push']
            })

    def _push_force(self, context, candidates, branch):
        if branch['ahead'] > 0:
            candidates.append({
                'word': 'push --force',
                'abbr': 'push --force',
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#push', {'--force': True}]
            })

    def _pull(self, context, candidates, branch):
        if branch['behind'] > 0:
            candidates.append({
                'word': 'pull',
                'abbr': 'pull',
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#pull']
            })

    def _pull_rebase(self, context, candidates, branch):
        if branch['behind'] > 0:
            candidates.append({
                'word': 'pull --rebase',
                'abbr': 'pull --rebase',
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#pull', {'--rebase': True}]
            })

    def _fetch(self, context, candidates):
        candidates.append({
            'word': 'fetch --all --prune',
            'abbr': 'fetch --all --prune',
            'action__type': 'func',
            'action__func': 'gitto#run',
            'action__args': ['repo#fetch', {'--all': True, '--prune': True}]
        })

    def _status(self, context, candidates):
        candidates.append({
            'word': 'status',
            'abbr': 'status',
            'action__type': 'source',
            'action__source': [{'name': 'gitto/status', 'args': []}]
        })

    def _branch(self, context, candidates):
        candidates.append({
            'word': 'branch -a',
            'abbr': 'branch -a',
            'action__type': 'source',
            'action__source': [{'name': 'gitto/branch', 'args': ['-a']}]
        })

    def _log(self, context, candidates):
        candidates.append({
            'word': 'log',
            'abbr': 'log',
            'action__type': 'source',
            'action__source': [{'name': 'gitto/log', 'args': []}]
        })

