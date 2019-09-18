let s:current_working_dir = ''

function! denite_gitto#start(args)
  let s:current_working_dir = g:gitto#config.get_buffer_path()
  execute printf('Denite %s', a:args)
endfunction

function! denite_gitto#run(feature, ...)
  return call(function('gitto#run_in_dir'), [s:current_working_dir, a:feature] + a:000)
endfunction

function! denite_gitto#commit(paths, amend)
  return gitto#view#commit_in_dir(s:current_working_dir, a:paths, a:amend)
endfunction

function! denite_gitto#diff_file_with_hash(path, info)
  return gitto#view#diff_file_with_hash_in_dir(s:current_working_dir, a:path, a:info)
endfunction

function! denite_gitto#diff_hash_with_hash(info1, info2)
  return gitto#view#diff_hash_with_hash_in_dir(s:current_working_dir, a:info1, a:info2)
endfunction

