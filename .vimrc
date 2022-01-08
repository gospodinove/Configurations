" vim-plug manager
call plug#begin()
         
" NerdTree
Plug 'preservim/NERDTree'
" Fuzzy Find
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
" morhetz colorscheme
Plug 'sainnhe/gruvbox-material'

call plug#end()

" line numbers
set number
" syntax highlighting
syntax on

" theme
set background=dark
colorscheme gruvbox-material

" tabs
set tabstop=2
set expandtab " replace tab with spaces
set softtabstop=2 " remove multiple whitespaces at once
set autoindent

" highlight current line
set cursorline
