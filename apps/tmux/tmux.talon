win.title: /tmux /
--
[vertical] split:
    key(ctrl-space)
    insert("%")

horizontal [split]:
    key(ctrl-space)
    insert("\"")

pick pane:
    key(ctrl-space)
    insert(":display-panes -d 3000\n")

new window:
    key(ctrl-space)
    insert("c")
