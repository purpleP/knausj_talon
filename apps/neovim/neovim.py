# import pynvim as vi

from talon import Context, Module, actions


mod = Module()
mod.apps.neovim = 'app.name: neovim'

mod.tag('vim_insert', 'Insert mode in vim')
mod.tag('vim_normal', 'Insert mode in vim')

verbs = {
    'delete': 'd',
    'change': 'c',
    'cut': 'x',
    'cut back': 'X',
    'comment': 'gc',
    'exchange': 'cx',
    'select': 'v',
}

line_verbs = {
    'indent': '>',
    'dedent': '<',
    'filter': '=',
    'format': 'gq',
    'select line': 'V',
}

line_motions = {
    'up': 'k',
    'down': 'j',
}

only_text_objects = {
    'paragraph': 'p',
    'quotes': "'",
    'double quotes': '"',
}

text_objects_and_motions = {
    'word': 'w',
    'big': 'W',
    'back': 'b',
    'big back': 'B',
    'end': 'e',
    'big end': 'E',
}

only_motions = {
    'up': 'k',
    'down': 'j',
    'left': 'h',
    'right': 'l',
    'search': '/',
    'search back': '?',
    'again': ';',
    'come back': ',',
    'next end of function': ']M',
    'previous end of function': '[M',
    'next start of function': ']m',
    'previous start of function': '[m',
}

motions_with_letter = {
    'untill': 't',
    'back untill': 'T',
    'to': 'f',
    'back to': 'F',
}

text_object_modifiers = {
    'a': 'a',
    'around': 'a',
    'inner': 'i',
    'linewise': 'V',
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

@mod.capture(rule='{self.vim_verbs} [<number>] {self.vim_motions_with_letter} <user.letter>')
def vim_verb_count_motion_letter(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))

@mod.capture(rule='[<number>] {self.vim_motions_with_letter} <user.letter>')
def vim_count_motion_letter(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))

@mod.capture(rule='[<number>] {self.vim_motions}')
def vim_count_motion(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))

@mod.capture(rule='{self.vim_line_verbs} [<number>] {self.vim_line_motions}')
def vim_count_verb_line_object(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))

@mod.capture(rule='{self.vim_verbs} [<number>] [{self.vim_text_object_modifiers}] ({self.vim_text_objects_and_motions} | {self.vim_text_objects} | {self.vim_motions})')
def vim_count_verb_object(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))

mod.list('vim_verbs', 'Vim counted verbs')
normal_mode_context.lists['self.vim_verbs'] = {**verbs}

mod.list('vim_text_objects', 'Vim text objects')
normal_mode_context.lists['self.vim_text_objects'] = {**only_text_objects}

mod.list('vim_text_objects_and_motions', 'Vim text objects and motions')
normal_mode_context.lists['self.vim_text_objects_and_motions'] = {**text_objects_and_motions}

mod.list('vim_text_object_modifiers', 'Vim text object modifiers')
normal_mode_context.lists['self.vim_text_object_modifiers'] = {**text_object_modifiers}

mod.list('vim_line_verbs', 'Vim line verbs')
normal_mode_context.lists['self.vim_line_verbs'] = {**line_verbs}

mod.list('vim_line_motions', 'Vim line motions')
normal_mode_context.lists['self.vim_line_motions'] = {**line_motions}

mod.list('vim_motions', 'Vim motions')
normal_mode_context.lists['self.vim_motions'] = {**only_motions, **text_objects_and_motions}

mod.list('vim_motions_with_letter', 'Vim motions with letter')
normal_mode_context.lists['self.vim_motions_with_letter'] = {**motions_with_letter}

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
