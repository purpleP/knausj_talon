import pynvim as vi

from talon import Context, Module, actions


mod = Module()

mod.tag('vim_insert', 'Insert mode in vim')
mod.tag('vim_normal', 'Insert mode in vim')

@mod.action_class
class Actions:
    def vim_paste(key):
        pass

insert_mode_context = Context()
ctx.matches = r'''
app: neovim
tag: user.vim_insert
'''

normal_mode_context = Context()
ctx.matches = r'''
app: neovim
tag: user.vim_normal
'''



@insert_mode_context.action_class
class Actions:
    def vim_paste(key):
        actions.key("ctrl-r")
        actions.next(key) # performs the next action implementation in the chai

@normal_mode_context.action_class
class Actions:
    def vim_paste(key):
        actions.key('"')
        actions.key(key or '"')
        actions.key('p')
        ctx.tags = ['user.vim_insert']
