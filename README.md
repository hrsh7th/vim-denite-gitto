# denite-gitto
denite.nvim + vim-gitto

# Install
```
call dein#add('Shougo/denite.nvim')
call dein#add('hrsh7th/vim-gitto')
call dein#add('hrsh7th/vim-denite-gitto')
```

NOTE: you can use other plugin managers.

# Setting
```
let g:gitto#config = {}
function! g:gitto#config.get_buffer_path()
  if exists('b:denite_context')
    return fnamemodify(bufname(winbufnr(b:denite_context.prev_winid)), ':p')
  endif
  return expand('%:p') " or getcwd() if you use vim-tabpagecd
endfunction
```

# Usage

This plugin provided vim's command.
The command signature is same of denite.

```
DeniteGitto `source-name`
```

# API
## `DeniteGitto gitto`
listing below actions

- push
- push force
- set_upstream_to
- status
- branch
- log

## `DeniteGitto gitto/status`

listing current git repo's statuses.

### actions
- reset
- checkout
- rm
- add
- commit
- diff (it show vimdiff)


## `DeniteGitto gitto/log`

liting current git repo's logs.

### actions
- reset
- reset_soft
- reset_hard
- changes
- changes_to_head

## `DeniteGitto gitto/changes`

### args
- 0: from revision
- 1: to revision

listing changed files in range.

### actions
- diff

## `DeniteGitto gitto/branch`

listing current git repo's branches.

### actions
- push
- push_force
- checkout
- rename
- new
- merge
- merge_no_ff
- rebase

# todo
- create `DeniteGitto gitto/stash`
- error handling if command failed via current working tree's changes.
- more helpful messages
- handling branches by instance instead of branch-name.

