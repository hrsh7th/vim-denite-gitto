# denite-gitto
denite.nvim + vim-gitto

# install
- you can use any plugin manager.
- this required below plugins.
  - Shougo/denite.nvim
  - hrsh7th/vim-gitto

# usage
## `Denite gitto/status`

listing current git repo's status.

### actions
- reset
- checkout
- rm
- add
- commit
- diff (it show vimdiff)


## `Denite gitto/log`

liting current git repo's log.
NOTE: it is development stage.


# todo
- create `Denite gitto/stash`
- create `Denite gitto/branch`
- create `Denite gitto/log` more actions(reset_hard, reset_soft).
- create `Denite gitto` to show useful menus.
- ability those methods
  - push
  - rebase
  - merge
  - fetch?

