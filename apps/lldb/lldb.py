<<<<<<< HEAD
from talon import Context, actions

ctx = Context()

ctx.matches = r"""
tag: user.lldb
"""

@ctx.action_class
class UserActions:
    ##
    # Generic debugger actions
    ##

    # Code execution
    def debugger_step_into():
        actions.auto_insert("stepi\n")

    def debugger_step_over():
        actions.auto_insert("nexti\n")

    def debugger_step_line():
        actions.auto_insert("step\n")

    def debugger_step_over_line():
        actions.auto_insert("next\n")

    def debugger_step_out():
        actions.auto_insert("finish\n")

    def debugger_continue():
        actions.auto_insert("c\n")

    def debugger_stop():
        actions.key("ctrl-c")

    def debugger_start():
        actions.auto_insert("run\n")

    def debugger_restart():
        actions.auto_insert("run\n")

    # XXX -
    def debugger_detach():
        actions.auto_insert("")

    # Registers
    def debugger_show_registers():
        actions.auto_insert("register read --all\n")

    def debugger_get_register():
        actions.auto_insert("register read ")

    def debugger_set_register():
        actions.user.auto_insert("register write ")
        # Breakpoints

    def debugger_show_breakpoints():
        actions.auto_insert("breakpoint list\n")

    def debugger_add_sw_breakpoint():
        actions.auto_insert("break ")

    # XXX -
    def debugger_add_hw_breakpoint():
        actions.auto_insert("")

    def debugger_break_now():
        actions.key("ctrl-c")

    def debugger_break_here():
        actions.auto_insert("break\n")

    def debugger_clear_all_breakpoints():
        actions.auto_insert("d br\n")

    def debugger_clear_breakpoint():
        actions.insert("d br ")

    def debugger_enable_all_breakpoints():
        actions.insert("br en\n")

    def debugger_enable_breakpoint():
        actions.insert("br en ")

    def debugger_disable_all_breakpoints():
        actions.insert("br dis\n")

    def debugger_disable_breakpoint():
        actions.insert("br dis ")

    def debugger_clear_breakpoint_id(number_small: int):
        actions.insert(f"br del {number_small}\n")

    def debugger_disable_breakpoint_id(number_small: int):
        actions.insert(f"br dis {number_small}\n")

    def debugger_enable_breakpoint_id(number_small: int):
        actions.insert(f"br en {number_small}\n")
||||||| parent of d5d1a202 (Add lldb support)
=======
from talon import Context, actions

ctx = Context()

ctx.matches = r"""
tag: user.lldb
"""

@ctx.action_class("debugger")
class UserActions:
    ##
    # Generic debugger actions
    ##

    # Code execution
    def debugger_step_into():
        actions.auto_insert("stepi\n")

    def debugger_step_over():
        actions.auto_insert("nexti\n")

    def debugger_step_line():
        actions.auto_insert("step\n")

    def debugger_step_over_line():
        actions.auto_insert("next\n")

    def debugger_step_out():
        actions.auto_insert("finish\n")

    def debugger_continue():
        actions.auto_insert("c\n")

    def debugger_stop():
        actions.key("ctrl-c")

    def debugger_start():
        actions.auto_insert("run\n")

    def debugger_restart():
        actions.auto_insert("run\n")

    # XXX -
    def debugger_detach():
        actions.auto_insert("")

    # Registers
    def debugger_show_registers():
        actions.auto_insert("register read --all\n")

    def debugger_get_register():
        actions.auto_insert("register read ")

    def debugger_set_register():
        actions.user.auto_insert("register write ")
        # Breakpoints

    def debugger_show_breakpoints():
        actions.auto_insert("breakpoint list\n")

    def debugger_add_sw_breakpoint():
        actions.auto_insert("break ")

    # XXX -
    def debugger_add_hw_breakpoint():
        actions.auto_insert("")

    def debugger_break_now():
        actions.key("ctrl-c")

    def debugger_break_here():
        actions.auto_insert("break\n")

    def debugger_clear_all_breakpoints():
        actions.auto_insert("d br\n")

    def debugger_clear_breakpoint():
        actions.insert("d br ")

    def debugger_enable_all_breakpoints():
        actions.insert("br en\n")

    def debugger_enable_breakpoint():
        actions.insert("br en ")

    def debugger_disable_all_breakpoints():
        actions.insert("br dis\n")

    def debugger_disable_breakpoint():
        actions.insert("br dis ")

    def debugger_clear_breakpoint_id(number_small: int):
        actions.insert(f"br del {number_small}\n")

    def debugger_disable_breakpoint_id(number_small: int):
        actions.insert(f"br dis {number_small}\n")

    def debugger_enable_breakpoint_id(number_small: int):
        actions.insert(f"br en {number_small}\n")
>>>>>>> d5d1a202 (Add lldb support)
