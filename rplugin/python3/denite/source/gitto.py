from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto'
        self.kind = 'gitto'
        self.vars = {}

    def gather_candidates(self, context):
        candidates = []
        self._status(context, candidates)
        self._branch(context, candidates)
        self._log(context, candidates)
        self._push(context, candidates)
        self._push_force(context, candidates)
        self._pull(context, candidates)
        self._pull_rebase(context, candidates)
        return [candidate for candidate in candidates if candidate]

    def _push(self, context, candidates):
        candidates.append({
            'word': 'push',
            'abbr': 'push',
            'action__type': 'func',
            'action__func': 'gitto#run',
            'action__args': ['branch#push']
        })

    def _push_force(self, context, candidates):
        candidates.append({
            'word': 'push --force',
            'abbr': 'push --force',
            'action__type': 'func',
            'action__func': 'gitto#run',
            'action__args': ['branch#push', {'--force': True}]
        })

    def _pull(self, context, candidates):
        candidates.append({
            'word': 'pull',
            'abbr': 'pull',
            'action__type': 'func',
            'action__func': 'gitto#run',
            'action__args': ['branch#pull']
        })

    def _pull_rebase(self, context, candidates):
        candidates.append({
            'word': 'pull --rebase',
            'abbr': 'pull --rebase',
            'action__type': 'func',
            'action__func': 'gitto#run',
            'action__args': ['branch#pull', {'--rebase': True}]
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
            'word': 'branch',
            'abbr': 'branch',
            'action__type': 'source',
            'action__source': [{'name': 'gitto/branch', 'args': []}]
        })

    def _log(self, context, candidates):
        candidates.append({
            'word': 'log',
            'abbr': 'log',
            'action__type': 'source',
            'action__source': [{'name': 'gitto/log', 'args': []}]
        })

