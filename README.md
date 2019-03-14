# denite-gitto
denite.nvim + vim-gitto

# Install
```
call dein#add('Shougo/denite.nvim')
call dein#add('hrsh7th/vim-gitto')
call dein#add('hrsh7th/vim-denite-gitto')
```

NOTE: you can use other plugin managers.

# API
## `Denite gitto`
listing below actions

- push
- push force
- status
- branch
- log

## `Denite gitto/status`

listing current git repo's statuses.

### actions
- reset
- checkout
- rm
- add
- commit
- diff (it show vimdiff)


## `Denite gitto/log`

liting current git repo's logs.

### actions
- reset
- reset_soft
- reset_hard
- changes
- changes_to_head

## `Denite gitto/changes`

### args
- 0: from revision
- 1: to revision

listing changed files in range.

### actions
- diff

## `Denite gitto/branch`

listing current git repo's branches.

### actions
- push
- checkout
- rename
- new
- merge
- merge_no_ff
- rebase

# todo
- create `Denite gitto/stash`
- supports below actions
  - fetch?
  - pull
- error handling if command failed via current working tree's changes.
- more helpful messages
