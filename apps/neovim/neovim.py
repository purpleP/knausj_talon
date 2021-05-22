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

@mod.capture(rule='({self.vim_non_register_verbs} | {self.vim_register_verbs}) [<number>]  ([{self.vim_text_object_modifiers}] {self.vim_text_object} | {self.vim_motions})')
def vim_non_register_verb_count_motion(parts) -> str:
    """Returns motions"""
    return ''.join(map(str, parts))


@mod.capture(rule='[<number>] {self.vim_motions}')
def vim_count_motion(parts) -> str:
    """Returns motions"""
    return ''.join(map(str, parts))

mod.list('vim_register_verbs', 'Vim register verb')
normal_mode_context.lists['self.vim_register_verbs'] = {
    'change': 'c',
    'copy': 'y',
    'cut': 'x',
    'cut back': 'X',
    'delete': 'd',
    'substitute': 's',
}


@mod.capture(rule='{self.vim_register_verbs} [<number>] ([{self.vim_text_object_modifiers}] {self.vim_text_object} | {self.vim_motions}) into (<user.letter>|<digits>|<user.symbol_key>)')
def vim_count_register_verb_object(parts: str) -> str:
    """Returns action"""
    *rest, _, register = parts
    return ''.join(['"', register, *rest])


@mod.capture(rule='{self.vim_register_verbs} [<number>] ([{self.vim_text_object_modifiers}] {self.vim_text_object} | {self.vim_motions})')
def vim_count_verb_object_default(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))


mod.list('vim_non_register_verbs', 'Vim non-register verb')
normal_mode_context.lists['self.vim_non_register_verbs'] = {
    'select': 'v',
    'comment': 'gc',
    'exchange': 'cx',
    'filter': '=',
    'indent': '>',
    'dedent': '<',
}

mod.list('vim_text_object_modifiers', 'Vim text object modifiers')
normal_mode_context.lists['self.vim_text_object_modifiers'] = {
    'a': 'a',
    'inner': 'i',
    'linewise': 'V',
}

mod.list('vim_text_object', 'Vim text object or motion')
normal_mode_context.lists['self.vim_text_object'] = {
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
}

mod.list('vim_mark_motions', 'Vim mark motion')
normal_mode_context.lists['self.vim_mark_motions'] = {
    'go mark': '`',
    'go mark line': "'",
}


@mod.capture(rule='[({self.vim_non_register_verbs} | {self.vim_register_verbs})] {self.vim_mark_motions} (<user.letter>|<digits>|<user.symbol_key>)')
def vim_mark_motion(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))


mod.list('vim_motions_with_character', 'Vim motion with character')
normal_mode_context.lists['self.vim_motions_with_character'] = {
    'to': 'f',
    'back to': 'F',
    'untill': 't',
    'back untill': 'T',
}


@mod.capture(rule='{self.vim_register_verbs} {self.vim_motions_with_character} (<user.letter>|<digits>|<user.symbol_key>) [<number>]')
def vim_register_verb_motion_with_character_character_count(parts: str) -> str:
    """Returns action"""
    verb, motion, char, *number, into, register  = parts
    return ''.join(map(str, [verb, *number, motion, char]))

@mod.capture(rule='{self.vim_register_verbs} {self.vim_motions_with_character} (<user.letter>|<digits>|<user.symbol_key>) [<number>] into (<user.letter>|<digits>|<user.symbol_key>)')
def vim_register_verb_motion_with_character_character_count(parts: str) -> str:
    """Returns action"""
    verb, motion, char, *number, into, register  = parts
    return ''.join(map(str, [f'"{register}', verb, *number, motion, char]))


@mod.capture(rule='({self.vim_non_register_verbs}| {self.vim_register_verbs}) {self.vim_motions_with_character} (<user.letter>|<digits>|<user.symbol_key>) [<number>]')
def vim_non_register_verb_motion_with_character_character_count(parts: str) -> str:
    """Returns action"""
    verb, motion, char, *number = parts
    return ''.join(map(str, [verb, *number, motion, char]))


@mod.capture(rule='{self.vim_motions_with_character} (<user.letter>|<digits>|<user.symbol_key>) [<number>]')
def vim_motion_with_character_character_count(parts: str) -> str:
    """Returns action"""
    motion, char, *number = parts
    return ''.join(map(str, [*number, motion, char]))


mod.list('vim_motions', 'Vim motion')
normal_mode_context.lists['self.vim_motions'] = {
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
    'screen top': 'H',
    'screen middle': 'M',
    'screen low': 'L',
    'top': 'gg',
    'bottom': 'G',
}

mod.list('vim_search_motions', 'Vim search motion')
normal_mode_context.lists['self.vim_search_motions'] = {
    'search': '/',
    'search back': '?',
}

@mod.capture(rule='[<number>] {self.vim_search_motions} phrase <user.text>')
def vim_search_phrase(parts: str) -> str:
    """Returns action"""
    *number, search, _, phrase = parts
    return ''.join(map(str, [*number, search, phrase]))


@mod.capture(rule='[<number>] {self.vim_search_motions} [<user.letters>]')
def vim_search_letters(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))


mod.list('vim_simple_verbs', 'Vim search motion')
normal_mode_context.lists['self.vim_simple_verbs'] = {
    'cut': 'x',
    'cut back': 'X',
}


@mod.capture(rule='[<number>] {self.vim_simple_verbs}')
def vim_simple_verbs(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))


mod.list('vim_paste_verbs', 'Vim search motion')
normal_mode_context.lists['self.vim_paste_verbs'] = {
    'paste': 'p',
    'paste before': 'P',
}


@mod.capture(rule='[<number>] {self.vim_paste_verbs}')
def vim_paste(parts: str) -> str:
    """Returns action"""
    return ''.join(map(str, parts))


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
