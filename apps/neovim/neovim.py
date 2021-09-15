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

@mod.capture(rule='({self.vim_non_register_verbs} | {self.vim_register_verbs}) [<number>] ([{self.vim_text_object_modifiers}] {self.vim_text_object} | [{self.vim_verb_motion_modifiers}] {self.vim_motions})')
def vim_non_register_verb_count_motion(match) -> str:
    """Returns motions"""
    return ''.join(map(str, match))


@mod.capture(rule='[<number>] {self.vim_motions}')
def vim_count_motion(match) -> str:
    """Returns motions"""
    return ''.join(map(str, match))

mod.list('vim_register_verbs', 'Vim register verb')
normal_mode_context.lists['self.vim_register_verbs'] = {
    'change': 'c',
    'copy': 'y',
    'cut': 'x',
    'cut back': 'X',
    'delete': 'd',
    'substitute': 's',
}


@mod.capture(rule='{self.vim_register_verbs} [<number>] ([{self.vim_text_object_modifiers}] {self.vim_text_object} | [{self.vim_verb_motion_modifiers}] {self.vim_motions}) into (<user.letter>|<digits>|<user.symbol_key>)')
def vim_count_register_verb_object(match) -> str:
    """Returns action"""
    *rest, _, register = match
    return ''.join(['"', register, *rest])


@mod.capture(rule='{self.vim_register_verbs} [<number>] ([{self.vim_text_object_modifiers}] {self.vim_text_object} | [{self.vim_verb_motion_modifiers}] {self.vim_motions})')
def vim_count_verb_object_default(match) -> str:
    """Returns action"""
    return ''.join(map(str, match))


mod.list('vim_non_register_verbs', 'Vim non-register verb')
normal_mode_context.lists['self.vim_non_register_verbs'] = {
    'select': 'v',
    'comment': 'gc',
    'exchange': 'cx',
    'to lower': 'gu',
    'to upper': 'gU',
    'swap case': '~',
    'filter': '=',
    'indent': '>',
    'dedent': '<',
}

mod.list('vim_verb_motion_modifiers', 'Vim verb modifiers')
normal_mode_context.lists['self.vim_verb_motion_modifiers'] = {
    'linewise': 'V',
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
def vim_mark_motion(match) -> str:
    """Returns action"""
    return ''.join(map(str, match))


mod.list('vim_motions_with_character', 'Vim motion with character')
normal_mode_context.lists['self.vim_motions_with_character'] = {
    'to': 'f',
    'back to': 'F',
    'untill': 't',
    'back untill': 'T',
}

@mod.capture(rule='{self.vim_register_verbs} [{self.vim_verb_motion_modifiers}] {self.vim_motions_with_character} (<user.letter>|<digits>|<user.symbol_key>) [<number>]')
def vim_register_verb_motion_with_character_character_count(match) -> str:
    """Returns action"""
    verb, motion, char, *number, into, register  = match
    return ''.join(map(str, [verb, *number, motion, char]))

@mod.capture(rule='{self.vim_register_verbs} [{self.vim_verb_motion_modifiers}] {self.vim_motions_with_character} (<user.letter>|<digits>|<user.symbol_key>) [<number>] into (<user.letter>|<digits>|<user.symbol_key>)')
def vim_register_verb_motion_with_character_character_count(match) -> str:
    """Returns action"""
    verb, motion, char, *number, into, register  = match
    return ''.join(map(str, [f'"{register}', verb, *number, motion, char]))


@mod.capture(rule='({self.vim_non_register_verbs}| {self.vim_register_verbs}) [{self.vim_verb_motion_modifiers}] (<user.letter>|<digits>|<user.symbol_key>) [<number>]')
def vim_non_register_verb_motion_with_character_character_count(match) -> str:
    """Returns action"""
    verb, motion, char, *number = match
    return ''.join(map(str, [verb, *number, motion, char]))


@mod.capture(rule='{self.vim_motions_with_character} (<user.letter>|<digits>|<user.symbol_key>) [<number>]')
def vim_motion_with_character_character_count(match) -> str:
    """Returns action"""
    motion, char, *number = match
    return ''.join(map(str, [*number, motion, char]))


mod.list('vim_motions', 'Vim motion')
normal_mode_context.lists['self.vim_motions'] = {
    'word': 'w',
    'matching': '%',
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
    'next start of method': ']m',
    'next end of method': ']M',
    'previous start of method': '[m',
    'previous end of method': '[M',
    'unmatched closing parenthesis': '[)',
    'unmatched open brace': '[{',
    'unmatched closing brace': '[}',
    'screen top': 'H',
    'screen middle': 'M',
    'screen low': 'L',
    'line up': 'k',
    'line down': 'j',
    'left': 'h',
    'right': 'l',
    'top': 'gg',
    'bottom': 'G',
}

mod.list('vim_search_motions', 'Vim search motion')
normal_mode_context.lists['self.vim_search_motions'] = {
    'search': '/',
    'search back': '?',
}

@mod.capture(rule='[<number>] {self.vim_search_motions} phrase <user.text>')
def vim_search_phrase(match) -> str:
    """Returns action"""
    return ''.join(map(str, [getattr(match, 'number', ''), match.vim_search_motions, match.text]))


@mod.capture(rule='[<number>] {self.vim_search_motions} <user.format_text>')
def vim_search_formatted_text(match) -> str:
    """Returns action"""
    return ''.join(map(str, [getattr(match, 'number', ''), match.vim_search_motions, match.format_text]))


@mod.capture(rule='[<number>] {self.vim_search_motions} [<user.letters>]')
def vim_search_letters(match) -> str:
    """Returns action"""
    return ''.join(map(str, match))


mod.list('vim_simple_verbs', 'Vim simple verbs')
normal_mode_context.lists['self.vim_simple_verbs'] = {
    'cut': 'x',
    'cut back': 'X',
}


@mod.capture(rule='[<number>] {self.vim_simple_verbs}')
def vim_simple_verbs(match) -> str:
    """Returns action"""
    return ''.join(map(str, match))


mod.list('vim_paste_verbs', 'Vim paste verbs')
normal_mode_context.lists['self.vim_paste_verbs'] = {
    'paste': 'p',
    'paste before': 'P',
    'paste indented': ']p',
    'paste indented before': '[p',
}


@mod.capture(rule='[<number>] {self.vim_paste_verbs} [from (<user.letter>|<digits>|<user.symbol_key>)]')
def vim_paste(match) -> str:
    """Returns action"""
    number = getattr(match, 'number', '')
    parts = [number, match.vim_paste_verbs]
    if len(match) == 4 or len(match) == 3:
        parts.append(match[-1])
    return ''.join(map(str, parts))


mod.list('vim_run_macro_verbs', 'Vim run macro verbs')
normal_mode_context.lists['self.vim_run_macro_verbs'] = {
    'run macro': '@',
}


@mod.capture(rule='[<number>] {self.vim_run_macro_verbs} [from (<user.letter>|<digits>)]')
def vim_run_macro(match) -> str:
    """Returns action"""
    number = getattr(match, 'number', '')
    parts = [number, match.vim_run_macro_verbs]
    if len(match) == 4 or len(match) == 3:
        parts.append(match[-1])
    else:
        parts.append('@')
    return ''.join(map(str, parts))


mod.list('vim_record_macro_verbs', 'Vim record macro verbs')
normal_mode_context.lists['self.vim_record_macro_verbs'] = {
    'record macro': 'q',
}


@mod.capture(rule='{self.vim_record_macro_verbs} [into (<user.letter>|<digits>)]')
def vim_record_macro(match) -> str:
    """Returns action"""
    parts = [match.vim_record_macro_verbs]
    if len(match) == 3:
        parts.append(match[-1])
    else:
        parts.append('q')
    return ''.join(map(str, parts))


mod.list('vim_quickfix', 'Vim record macro verbs')
normal_mode_context.lists['self.vim_record_macro_verbs'] = {
    'record macro': 'q',
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
