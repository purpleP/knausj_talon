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

<user.vim_search_phrase>$:
    insert("{vim_search_phrase}")

<user.vim_search_letters>$:
    insert("{vim_search_letters}")

<user.vim_register_verb_motion_with_character_character_count>$:
    insert("{vim_register_verb_motion_with_character_character_count}")

<user.vim_simple_verbs>$:
    insert("{vim_simple_verbs}")

<user.vim_paste>$:
    insert("{vim_paste}")

<user.vim_run_macro>$:
    insert("{vim_run_macro}")

<user.vim_record_macro>$:
    insert("{vim_record_macro}")

<user.vim_search_formatted_text>$:
    insert("{vim_search_formatted_text}")

line before: user.vim_line_before()
line after: user.vim_line_after()
insert: key(i)
append: key(a)
before: key(I)
after: key(A)

# actions
undo: insert("u")
redo: key(ctrl-r)


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

jump out: key("ctrl-o")
jump in: key("ctrl-i")

jump to current error: insert(":cc\n")

jump to error <number>:
    insert(":cc ")
    insert(number)
    insert("\n")

jump to current location: insert(":ll\n")

jump to location <number>:
    insert(":ll ")
    insert(number)
    insert("\n")

jump to previous error [<number>]:
    insert(":")
    insert(number or 1)
    insert("cprevious\n")

jump to next error [<number>]:
    insert(":")
    insert(number or 1)
    insert("cnext\n")

jump to previous location [<number>]:
    insert(":")
    insert(number or 1)
    insert("lprevious\n")

jump to next location [<number>]:
    insert(":")
    insert("lnext\n")

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

open fixes: insert(":copen\n")
close fixes: insert(":ccl\n")
close locatons : insert(":ccl\n")

git status: insert(":G\n")
git commit: insert(":G commit\n")
git push: insert(":G push\n")
git push force: insert(":G push --force\n")

alternate file: key(ctrl-^)
