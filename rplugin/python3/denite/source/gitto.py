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
        return {
            'word': 'push',
            'abbr': 'push',
            'action__command': 'call gitto#do("branch#push")()'
        }

    def _push_force(self, context):
        return {
            'word': 'push force',
            'abbr': 'push force',
            'action__command': 'call gitto#do("branch#push")({ "--force": v:true })'
        }

    def _status(self, context):
        return {
            'word': 'status',
            'abbr': 'status',
            'action__command': 'Denite gitto/status'
        }

    def _log(self, context):
        return {
            'word': 'log',
            'abbr': 'log',
            'action__command': 'Denite gitto/log'
        }

