from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto/log'
        self.kind = 'gitto/log'
        self.vars = {}

    def gather_candidates(self, context):
        logs = self.vim.call('gitto#run', 'log#get')
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

