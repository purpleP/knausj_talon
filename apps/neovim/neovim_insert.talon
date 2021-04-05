app: neovim
win.title: /VIM MODE:i/
-
tag(): user.vim_insert

paste [from <user.any_alphanumeric_key>]:
    user.vim_paste_after(any_alphanumeric_key or '"')

delete word:
    key(ctrl-w)
