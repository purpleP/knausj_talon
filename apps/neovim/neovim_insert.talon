app: neovim
win.title: /VIM MODE:i/
-
tag(): user.vim_insert

paste [from <user.any_alphanumeric_key>]:
    user.vim_paste_after(any_alphanumeric_key or '"')

delete word:
    key(ctrl-w)

quotes:
    key(')
    key(')
    key(left)

double quotes:
    key(")
    key(")
    key(left)

expand:
    key(enter:2)
    edit.up()
    key(tab)

braces:
    key({)
    key(})
    key(left)

squares:
    key([)
    key(])
    key(left)

angles:
    key(<)
    key(>)
    key(left)

