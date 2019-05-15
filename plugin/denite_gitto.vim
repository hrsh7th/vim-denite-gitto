if exists('g:loaded_denite_gitto')
  finish
endif
let g:loaded_denite_gitto = v:true

command! -nargs=+ DeniteGitto call s:denite_gitto(<q-args>)
function! s:denite_gitto(args)
  call denite_gitto#start(a:args)
endfunction

