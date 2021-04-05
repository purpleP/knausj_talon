app: neovim
win.title: /VIM MODE:n/
-
tag(): user.vim_normal

line before: user.vim_line_before()
line after: user.vim_line_after()
insert: key(i)
append: key(a)
before: key(I)
after: key(A)

# verbs
delete: key(d)
change: key(c)
copy: key(y)
cut: key(x)
cut back: key(shift-x)
comment: insert("gc")
exchange: insert("cx")

around: key(a)
inside: key(i)

# text some-objects and motions

word: key(w)
end: key(e)
back: key(b)

big word: key(shift-w)
big end: key(shift-e)
big back: key(shift-b)

paragraph: key(p)

top: insert("gg")
bottom: insert("G")

till: key(t)

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
select [<number>] lines:
    insert(number + "V")
select line: insert("V")
start: key(^)
lend: key($)

move center: insert("zz")
move top: insert("zt")
move bottom: insert("zb")
move down: key(ctrl-y)
move up: key(ctrl-e)

quotes:
    key(')
    key(')
    key(left)

double quotes:
    key(")
    key(")
    key(left)

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

search: insert(":grep ")
find up: key(?)
find: key(/)
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
