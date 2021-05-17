# import pynvim as vi

from talon import Context, Module, actions


mod = Module()
mod.apps.neovim = '''
os: windows
and app.name: nvim-qt.exe
os: windows
and app.exe: nvim-qt.exe
os: linux
and app.name: neovim
'''

mod.tag('vim_insert', 'Insert mode in vim')
mod.tag('vim_normal', 'Normal mode in vim')

ctx = Context()
ctx.matches = r'''
app: vim
'''


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
        pass

    def vim_line_before():
        """Add line before current one"""
        pass

@mod.capture(rule='{self.vim_register_verbs} [<number>] [{self.vim_text_object_modifiers}] {self.vim_text_object_or_motion} into ({user.any_alphanumeric_key} | {user.symbol_key})')
def vim_register_verb_count_motion(parts) -> str:
    """Returns motions"""
    return ''.join(map(str, parts))

@mod.capture(rule='[<number>] {self.vim_motions}')
def vim_count_motion(parts) -> str:
    """Returns motions"""
    return ''.join(map(str, parts))

@mod.capture(rule='{self.vim_register_verbs} [<number>] [{self.vim_text_object_modifiers}] {self.vim_text_object_or_motion}')
def vim_count_register_verb_object(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))

@mod.capture(rule='{self.vim_register_verbs} [<number>] [{self.vim_text_object_modifiers}] {self.vim_text_object_or_motion} into ({user.any_alphanumeric_key} | {user.symbol_key})')
def vim_count_register_verb_object(parts: str) -> str:
    """Returns action"""
    *rest, _, register = parts
    return ''.join(['"', register, *rest])

mod.list('vim_register_verbs', 'Vim register verb')
normal_mode_context.lists['self.vim_register_verbs'] = {
    'change': 'c',
    'copy': 'y',
    'cut': 'x',
    'cut back': 'X',
    'substitute': 's'
}

mod.list('vim_text_object_modifiers', 'Vim text object modifiers')
normal_mode_context.lists['self.vim_text_object_modifiers'] = {
    'a': 'a',
    'inner': 'inner',
}

mod.list('vim_text_object_or_motion', 'Vim text object or motion')
normal_mode_context.lists['self.vim_text_object_or_motion'] = {
    'word': 'w',
    'big': 'W',
    'paragraph': 'p',
    'quotes': "'",
    'ticks': '`',
    'double quotes': '"',
    'curly': 'B',
    'braces': 'b',
    'block': ']',
    'angles': '>',
    'tag': 't',
    'screen top': 'H',
    'screen middle': 'M',
    'screen low': 'L',
    'top': 'gg',
    'bottom': 'G',
}

mod.list('vim_motion', 'Vim motion')
normal_mode_context.lists['self.motion'] = {
    'word': 'w',
    'big': 'W',
    'back': 'b',
    'big back': 'B',
    'tip': 'e',
    'big tip': 'E',
    'tail': 'ge',
    'big tail': 'gE',
}



mod.list('vim_verb', 'Vim verb')
normal_mode_context.lists['self.verb'] = {
}



mod.list('vim_motion', 'Vim motion')
normal_mode_context.lists['self.motion'] = {
    'word': 'w',
    'big': 'W',
    'back': 'b',
    'big back': 'B',
    'tip': 'e',
    'big tip': 'E',
    'tail': 'ge',
    'big tail': 'gE',
    'sentence': ')',
    'back sentence': '(',
    'section': ']]',
    'back section': '[[',
    'end section': '][',
    'end back section': '[]',
    'unmatched open parenthesis': '[(',
    'unmatched closing parenthesis': '[)',
    'unmatched open brace': '[{',
    'unmatched closing brace': '[}',
}



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

@insert_mode_context.action_class("win")
class win_actions_insert:
    def filename():
        title = actions.win.title()
        _, filename  = title.rsplit(")")
        # Assumes the last word after the last ) entry has the filename
        return filename if "." in filename else ""

@normal_mode_context.action_class("win")
class win_actions_normal:
    def filename():
        title = actions.win.title()
        _, filename  = title.rsplit(")")
        # Assumes the last word after the last ) entry has the filename
        return filename if "." in filename else ""
