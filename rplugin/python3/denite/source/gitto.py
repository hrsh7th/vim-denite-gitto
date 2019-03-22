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
        if not self.is_pushable(branches):
            return

        current = self.current_branch(branches)
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
        if not self.is_pushable(branches):
            return

        current = self.current_branch(branches)
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
        if not self.is_pullable(branches):
            return

        current = self.current_branch(branches)
        candidates.append({
            'word': ['pull', 'target is `{}`'.format(current['upstream'])],
            'action__type': 'func',
            'action__func': 'gitto#run',
            'action__args': ['repo#pull']
        })

    def _pull_rebase(self, context, candidates, branches):
        if not self.is_pullable(branches):
            return

        current = self.current_branch(branches)
        candidates.append({
            'word': ['pull rebase', 'target is `{}`'.format(current['upstream'])],
            'action__type': 'func',
            'action__func': 'gitto#run',
            'action__args': ['repo#pull', {'--rebase': True}]
        })

    def _set_upstream_to(self, context, candidates, branches):
        current = self.current_branch(branches)
        if not current or len(current['upstream']) > 0:
            return

        same_name = self._get_same_name_other_branch(current, branches)
        if same_name:
            candidates.append({
                'word': ['set-upstream-to', '`{}`'.format(
                    same_name['refname']
                )],
                'action__type': 'func',
                'action__func': 'gitto#run',
                'action__args': ['branch#set_upstream_to', same_name]
            })

    def _fetch(self, context, candidates):
        candidates.append({
            'word': ['fetch', 'fetch all and prune'],
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

    def _get_same_name_other_branch(self, target, branches):
        for branch in branches:
            if target['refname'] != branch['refname'] and target['name'] == branch['name']:
                return branch
        return None


    def current_branch(self, branches):
        return next((branch for branch in branches if branch['current']), None)

    def is_pullable(self, branches):
        current = self.current_branch(branches)
        if not current:
            return False
        if len(current['upstream']) <= 0:
            return False
        if current['behind'] <= 0:
            return False
        return True


    def is_pushable(self, branches):
        current = self.current_branch(branches)
        same_name = self._get_same_name_other_branch(current, branches)
        if not current:
            return False
        if not same_name:
            return True
        if len(current['upstream']) <= 0:
            return False
        if current['ahead'] <= 0:
            return False
        return True

