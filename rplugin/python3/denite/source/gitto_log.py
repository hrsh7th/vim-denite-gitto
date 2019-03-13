from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto/log'
        self.kind = 'gitto/log'
        self.vars = {
                'default_option': {
                        '--no-merges': True
                    }
                }

    def gather_candidates(self, context):
        logs = self.vim.call('gitto#run', 'log#get', self.vars['default_option'], context['args'][0] if len(context['args']) > 0 else '')
        if len(logs) <= 0:
            return []

        author_name_len = max([len(x['author_name']) for x in logs])
        return [{
            'word': '{:>20} | {:<{width}} | {}'.format(log['author_date'],
                                                       log['author_name'],
                                                       log['subject'],
                                                       width=author_name_len),
            'abbr': '{:>20} | {:<{width}} | {}'.format(log['author_date'],
                                                       log['author_name'],
                                                       log['subject'],
                                                       width=author_name_len),
            'action__log': log,
        } for log in logs]

