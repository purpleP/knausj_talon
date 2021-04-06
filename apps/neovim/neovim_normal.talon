app: neovim
win.title: /VIM MODE:n/
-
tag(): user.vim_normal

<user.vim_count_verb_line_object>$:
    insert("{vim_count_verb_line_object}")

<user.vim_count_verb_object>$:
    insert("{vim_count_verb_object}")

<user.vim_count_motion>$:
    insert("{vim_count_motion}")

<user.vim_verb_count_motion_letter>$:
    insert("{vim_verb_count_motion_letter}")

<user.vim_count_motion_letter>$:
    insert("{vim_count_motion_letter}")


line before: user.vim_line_before()
line after: user.vim_line_after()
insert: key(i)
append: key(a)
before: key(I)
after: key(A)

top: insert("gg")
bottom: insert("G")

# actions
undo: insert("u")
redo: key(ctrl-r)


paste [from <user.any_alphanumeric_key>]:
    user.vim_paste_after(any_alphanumeric_key or '"')
paste before [from <user.any_alphanumeric_key>]:
    user.vim_paste_before(any_alphanumeric_key or '"')

save changes: insert(":w\n")
change line: insert("S")
copy line: insert("yy")
comment line: insert("gcc")
delete line: insert("dd")
accept: key(ctrl-y)
edit: insert(":e ")

indent pasted: insert("=']") 
browse: insert(":Ex\n")

horizontal split:
    key(ctrl-w)
    key(s)

split:
    key(ctrl-w)
    key(v)

close window [<number>]:
    insert(number or "")
    key(ctrl-w)
    key(q)

window [<number>]:
    insert(number)
    key(ctrl-w)
    key(w)

maximize window:
    key(ctrl-w)
    key(_)

equalize windows:
    key(ctrl-w)
    key(=)

create tab: insert(":tabnew\n")

next tab:
    key(g)
    key(t)

previous tab:
    key(g)
    key(T)

references: insert("gr")  
definition: insert("gd")  
choose file: insert(":CocList files\n")
choose buffer: insert(":CocList buffers\n")

next error: insert(":cnext\n")
previous error: insert(":cprev\n")
next location: insert(":lnext\n")
previous location: insert(":lprev\n")
next hunk: insert("]c")
previous hunk: insert("[c")

show numbers: insert(":setl nu rnu\n")

scroll center: insert("zz")
scroll top: insert("zt")
scroll bottom: insert("zb")
scroll down: key(ctrl-y)
scroll up: key(ctrl-e)

close quick fix: insert(":ccl\n")

git status: insert(":Gstatus\n")
commit: insert(":Gcommit\n")

alternate file: key(ctrl-^)

substitute:
    insert(":s//")
    key(left)

substitute global:
    insert(":s//g")
    key(left)
    key(left)

substitute all:
    insert(":%s//g")
    key(left)
    key(left)
