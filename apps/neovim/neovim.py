# import pynvim as vi

from talon import Context, Module, actions


mod = Module()

mod.tag('vim_insert', 'Insert mode in vim')
mod.tag('vim_normal', 'Insert mode in vim')

@mod.action_class
class Actions:
    def vim_paste(key: str):
        """Some doc string"""
        pass

insert_mode_context = Context()
insert_mode_context.matches = r'''
app: neovim
tag: user.vim_insert
'''

normal_mode_context = Context()
normal_mode_context.matches = r'''
app: neovim
tag: user.vim_normal
'''



@insert_mode_context.action_class('self')
class InsertModeAction:
    def vim_paste(key: str):
        actions.key("ctrl-r")
        actions.next(key) # performs the next action implementation in the chai

@normal_mode_context.action_class('self')
class NormalModeActions:
    def vim_paste(key: str):
        actions.key('"')
        actions.key(key or '"')
        actions.key('p')
        ctx.tags = ['user.vim_insert']
