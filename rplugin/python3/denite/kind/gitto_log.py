from denite.kind.base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'gitto/log'
        self.redraw_actions = []
        self.persist_actions = self.redraw_actions

