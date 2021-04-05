# import pynvim as vi

from talon import Context, Module, actions


mod = Module()
mod.apps.neovim = 'app.name: neovim'

mod.tag('vim_insert', 'Insert mode in vim')
mod.tag('vim_normal', 'Insert mode in vim')

counted_verbs = {
    'delete': 'd',
}

text_objects = {
    'word': 'w',
    'big': 'W',
    'back': 'b',
    'big back': 'B',
}



@mod.action_class
class Actions:
    def vim_paste_before(key: str):
        """Paste from register before the cursor"""
        pass
    
    def vim_paste_after(key: str):
        """Paste from register after the cursor"""
        pass

    def vim_line_after():
        """Add line before current one"""
        actions.key('o')

    def vim_line_before():
        """Add line before current one"""
        actions.key('O')

insert_mode_context = Context()
insert_mode_context.matches = r'''
app.name: Neovim
tag: user.vim_insert
'''


normal_mode_context = Context()
normal_mode_context.matches = r'''
app.name: Neovim
tag: user.vim_normal
'''

@mod.capture(rule='{self.vim_counted_verbs} [<number>] {self.vim_text_objects}')
def count_verb_object(parts: str) -> str:
    return ''.join(map(str, parts))

mod.list('vim_counted_verbs', 'Vim counted verbs')
mod.list('vim_text_objects', 'Vim text objects')
normal_mode_context.lists['self.vim_counted_verbs'] = {**counted_verbs}
normal_mode_context.lists['self.vim_text_objects'] = {**text_objects}

@insert_mode_context.action_class('self')
class InsertModeAction:
    def vim_paste_after(key: str):
        actions.key('ctrl-r')
        actions.key(key or '"') # performs the next action implementation in the chai

@normal_mode_context.action_class('self')
class NormalModeActions:
    def vim_paste_before(key: str):
        actions.key('"')
        actions.key(key or '"')
        actions.key('P')
    
    def vim_paste_after(key: str):
        actions.key('"')
        actions.key(key or '"')
        actions.key('p')
    
    def vim_line_before():
        actions.key('O')
    
    def vim_line_after():
        actions.key('o')
