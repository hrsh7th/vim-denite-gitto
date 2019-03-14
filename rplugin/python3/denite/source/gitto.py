from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto'
        self.kind = 'command'
        self.vars = {}
        self.label_len = 18

    def gather_candidates(self, context):
        candidates = []
        candidates += [self._push(context)]
        candidates += [self._push_force(context)]
        candidates += [self._status(context)]
        candidates += [self._log(context)]
        return [candidate for candidate in candidates if candidate]

    def _push(self, context):
        branch = self.vim.call('gitto#run', 'branch#current')
        if not branch:
            return
        return {
            'word': '{:<{label}}: {} to {}'.format('push', branch['name'], branch['remote'], label=self.label_len),
            'abbr': '{:<{label}}: {} to {}'.format('push', branch['name'], branch['remote'], label=self.label_len),
            'action__command': 'call gitto#do("branch#push")({})'.format(branch['name'])
        }

    def _push_force(self, context):
        branch = self.vim.call('gitto#run', 'branch#current')
        if not branch:
            return
        return {
            'word': '{:<{label}}: {} to {}'.format('force push', branch['name'], branch['remote'], label=self.label_len),
            'abbr': '{:<{label}}: {} to {}'.format('force push', branch['name'], branch['remote'], label=self.label_len),
            'action__command': 'call gitto#do("branch#push")({}, {{ "--force": v:true }})'.format(branch['name'])
        }

    def _status(self, context):
        return {
            'word': '{:<{label}}: show current status'.format('status', label=self.label_len),
            'abbr': '{:<{label}}: show current status'.format('status', label=self.label_len),
            'action__command': 'Denite gitto/status'
        }

    def _log(self, context):
        return {
            'word': '{:<{label}}: show logs'.format('log', label=self.label_len),
            'abbr': '{:<{label}}: show logs'.format('log', label=self.label_len),
            'action__command': 'Denite gitto/log'
        }

