from talon import Module, Context

mod = Module()
mod.tag('cargo', desc='tag for enabling cargo commands')

ctx = Context()
ctx.matches = r'''
tag: user.cargo
'''

mod.list('cargo_action', desc='actions performed by cargo')
ctx.lists['self.cargo_action'] = {
    'build': 'build',
    'check': 'check',
    'run': 'run',
    'fix': 'fix',
    'clip': 'clippy',
    'format': 'fmt',
}
