win.title: /tmux /
--
[vertical] split:
    key(ctrl-space)
    insert("%")

horizontal [split]:
    key(ctrl-space)
    insert("\"")

next pane: key(ctrl-space o)

pick pane:
    key(ctrl-space)
    insert(":display-panes -d 3000\n")

new window:
    key(ctrl-space c)

pick window:
    key(ctrl-space w)

pick buffer:
    key(ctrl-space b)

copy mode:
    key(ctrl-space space)
