app: neovim
win.title: /VIM MODE:c/
-
tag(): user.vim_command

paste [from <user.any_alphanumeric_key>]:
    user.vim_paste_after(any_alphanumeric_key or '"')

kill word:
    key(ctrl-w)

quotes:
    key(':2)
    key(left)

double quotes:
    key(":2)
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

norm: key(esc)
