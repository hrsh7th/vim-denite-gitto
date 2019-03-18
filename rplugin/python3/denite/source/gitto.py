from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto'
        self.kind = 'gitto'
        self.vars = {}
        self.label_length = 18

    def gather_candidates(self, context):
        branches = self.vim.call('gitto#run', 'branch#get', {'-a': True})

        candidates = []
        self._status(context, candidates)
        self._branch(context, candidates)
        self._log(context, candidates)
        self._fetch(context, candidates)
        self._set_upstream_to(context, candidates, branches)
        self._push(context, candidates, branches)
        self._push_force(context, candidates, branches)
        self._pull(context, candidates, branches)
        self._pull_rebase(context, candidates, branches)

        for candidate in candidates:
            candidate.update({
                'word': '{:{label}} | {}'.format(*candidate['word'], label=self.label_length),
                'abbr': '{:{label}} | {}'.format(*candidate['word'], label=self.label_length)
            })
        return candidates

    def _push(self, context, candidates, branches):
        current = self.current_branch(branches)
        if current and (current['ahead'] > 0 or len(current['upstream']) <= 0):
            candidates.append({
                'word': ['push', 'target is `{}/{}`, {} commits: {}'.format(
                    current['remote'],
                    current['name'],
                    current['ahead'],
                    current['subject']
                )],
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#push']
            })

    def _push_force(self, context, candidates, branches):
        current = self.current_branch(branches)
        if current and (current['ahead'] > 0 or len(current['upstream']) <= 0):
            candidates.append({
                'word': ['push force', 'target is `{}/{}`, {} commits: {}'.format(
                    current['remote'],
                    current['name'],
                    current['ahead'],
                    current['subject']
                )],
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#push', {'--force': True}]
            })

    def _pull(self, context, candidates, branches):
        current = self.current_branch(branches)
        if current and len(current['upstream']) > 0 and current['behind'] > 0:
            candidates.append({
                'word': ['pull', 'target is `{}`'.format(current['upstream'])],
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#pull']
            })

    def _pull_rebase(self, context, candidates, branches):
        current = self.current_branch(branches)
        if current and len(current['upstream']) > 0 and current['behind'] > 0:
            candidates.append({
                'word': ['pull rebase', 'target is `{}`'.format(current['upstream'])],
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['repo#pull', {'--rebase': True}]
            })

    def _set_upstream_to(self, context, candidates, branches):
        current = self.current_branch(branches)
        if not current:
            return

        if len(current['upstream']) > 0:
            return

        for branch in branches:
            if not branch['local'] and current['name'] == branch['name']:
                candidates.append({
                    'word': ['set-upstream-to', '`{}`'.format(
                        branch['refname']
                    )],
                    'action__type': 'func',
                    'action__func': 'gitto#run',
                    'action__args': ['branch#set_upstream_to', branch]
                })
                break

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
            'word': ['branch', ''],
            'action__type': 'source',
            'action__source': [{'name': 'gitto/branch', 'args': ['-a']}]
        })

    def _log(self, context, candidates):
        candidates.append({
            'word': ['log', ''],
            'action__type': 'source',
            'action__source': [{'name': 'gitto/log', 'args': []}]
        })

    def current_branch(self, branches):
        return next((branch for branch in branches if branch['current']), None)

