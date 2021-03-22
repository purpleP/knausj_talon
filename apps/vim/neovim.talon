app: neovim

add above: insert("O")
add below: insert("o")
insert: key(i)
append: key(a)

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
paste: key(p)
paste before: key(P)
paste above: key(P)
save: insert(":w\n")
change line: insert("S")
copy line: insert("yy")
delete line: insert("dd")
join [<number>] lines: insert(number or "" + "J")
accept: key(ctrl-y)

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
close quick fix: insert(":ccl\n")

git status: insert(":Gstatus\n")
commit: insert(":Gcommit\n")

alternate file: key(ctrl-^)
