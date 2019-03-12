# denite-gitto
denite.nvim + vim-gitto

# install
```
call dein#add('Shougo/denite.nvim')
call dein#add('hrsh7th/vim-gitto')
call dein#add('hrsh7th/vim-denite-gitto')
```

NOTE: you can use other plugin managers.

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

