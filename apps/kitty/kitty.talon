app.name: kitty
--
tag(): user.file_manager
tag(): user.git
tag(): user.kubectl
tag(): user.cargo
tag(): terminal

suspend: key(ctrl-z)

jobs: insert("jobs\n")

foreground <number>: insert("fg {number or 1}\n")

background <number>: insert("bg {number or 1}\n")
