app: neovim
win.title: /VIM MODE:n/
-
tag(): user.vim_normal

<user.vim_non_register_verb_count_motion>$:
    insert("{vim_non_register_verb_count_motion}")

<user.vim_count_motion>$:
    insert("{vim_count_motion}")

<user.vim_count_verb_object_default>$:
    insert("{vim_count_verb_object_default}")

<user.vim_count_register_verb_object>$:
    insert("{vim_count_register_verb_object}")

<user.vim_motion_with_character_character_count>$:
    insert("{vim_motion_with_character_character_count}")

<user.vim_mark_motion>$:
    insert("{vim_mark_motion}")

<user.vim_non_register_verb_motion_with_character_character_count>$:
    insert("{vim_non_register_verb_motion_with_character_character_count}")

line before: user.vim_line_before()
line after: user.vim_line_after()
insert: key(i)
append: key(a)
before: key(I)
after: key(A)

# actions
undo: insert("u")
redo: key(ctrl-r)


paste [from <user.any_alphanumeric_key>]:
    user.vim_paste_after(any_alphanumeric_key or '"')
paste before [from <user.any_alphanumeric_key>]:
    user.vim_paste_before(any_alphanumeric_key or '"')

mark <user.any_alphanumeric_key>:
    insert("m" + any_alphanumeric_key)

save changes: insert(":w\n")
change line: insert("S")
change after: insert("C")
copy line: insert("yy")
comment line: insert("gcc")
delete line: insert("dd")
edit: insert(":e ")

indent pasted: insert("=']") 
browse: insert(":Ex\n")
reselect: insert("gv")

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
choose: insert(":Tele\n")
choose file: insert(":Tele find_files\n")
choose buffer: insert(":Tele buffers\n")
choose recent: insert(":Tele oldfiles\n")

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
scroll down [<number>]:
    insert(number or "")
    key(ctrl-y)
scroll up [<number>]:
    insert(number or "")
    key(ctrl-e)

close quick fix: insert(":ccl\n")

git status: insert(":G\n")
git commit: insert(":G commit\n")

alternate file: key(ctrl-^)
