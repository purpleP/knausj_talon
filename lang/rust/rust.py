from talon import Module, Context, actions, ui, imgui, settings

ctx = Context()
ctx.matches = r'''
mode: user.rust
mode: command 
and code.language: rust
'''

@ctx.action_class('user')
class user_actions:
    def code_default_function(text: str):
        result = f'fn {text}() -> () ' + '{}'
        actions.user.paste(result)
        for i in range(10):
            actions.edit.left()
