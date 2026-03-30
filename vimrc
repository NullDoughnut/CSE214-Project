colorscheme slate
set shiftwidth=4
set expandtab
set tabstop=4
set showmatch
set hls
set cursorcolumn
set bg=dark
syntax on
augroup BlackFormatting
	  autocmd!
	    autocmd BufWritePre *.py silent %!black -q -
augroup END

set listchars=eol:$,tab:>-,trail:~,extends:>,precedes:<,nbsp:☠,tab:▸␣
se number
