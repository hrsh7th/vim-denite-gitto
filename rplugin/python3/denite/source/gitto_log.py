from denite.source.base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gitto/log'
        self.kind = 'gitto/log'
        self.is_public_context = True
        self.vars = {}
        self.vars['option'] = {}

    def on_init(self, context):
        context['__path'] = context['args'][0] if len(context['args']) > 0 else ''

    def gather_candidates(self, context):
        logs = self.vim.call('denite_gitto#run', 'log#get', self.vars['option'], context['__path'])
        if not len(logs):
            return []

        lengths = self._column_len(logs, [
            'author_date',
            'author_name',
            'subject'
        ])

        return [{
            'word': '{:{author_date}} | {} | {:{author_name}} | {:{subject}}'.format(
                log['author_date'], log['commit_hash'][0:7], log['author_name'], log['subject'],
                author_date=lengths['author_date'],
                commit_hash=7,
                author_name=lengths['author_name'],
                subject=lengths['subject']
            ),
            'abbr': '{:{author_date}} | {} | {:{author_name}} | {:{subject}}'.format(
                log['author_date'], log['commit_hash'][0:7], log['author_name'], log['subject'],
                author_date=lengths['author_date'],
                commit_hash=7,
                author_name=lengths['author_name'],
                subject=lengths['subject']
            ),
            'action__log': log,
        } for log in logs]

    def _column_len(self, candidates, columns):
        lengths = {}
        for key in columns:
            lengths[key] = max([1] + [len(x[key]) for x in candidates])
        return lengths

