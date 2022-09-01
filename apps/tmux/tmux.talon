tag: user.tmux
-
tag(): user.splits

# pane management - these commands use the word split to match with the splits
# tag defined in tags/splits/splits.talon
go split <user.arrow_key>: user.tmux_keybind(arrow_key)
#Say a number after this command to switch to pane
go split: user.tmux_execute_command("display-panes -d 0")
--
[vertical] split:
    key(ctrl-space)
    insert("%")

horizontal [split]:
    key(ctrl-space)
    insert("\"")

next pane: key(ctrl-space o)

new window:
    key(ctrl-space c)

pick window:
    key(ctrl-space w)

pick buffer:
    key(ctrl-space b)

copy mode:
    key(ctrl-space space)
