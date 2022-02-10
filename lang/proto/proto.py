from talon import Context, Module

mod = Module()

ctx = Context()
ctx.matches = r"""
tag: user.protobuf
"""

ctx.lists["user.code_type"] = {
    "string": "string",
    "bytes": "bytes",
    "you sixty four": "uint64",
    "you thirty two": "uint32",
    "eye sixty four": "int64",
    "eye thirty two": "int32",
    "sin sixty four": "sint64",
    "sin thirty two": "sint32",
    "fixed sixty four": "fixed64",
    "fixed thirty two": "fixed32",
    "as fixed sixty four": "sfixed64",
    "as fixed thirty two": "sfixed32",
    "boolean": "bool",
    "double": "double",
    "float": "float",
}

@ctx.action_class('user')
class UserActions:
    def code_insert_function(text: str, selection: str):
        actions.user.paste(f'{text}({selection or ""})')
        actions.edit.left()

    def code_default_function(text: str):
        actions.insert('rpc ')
        formatter = settings.get('user.code_public_function_formatter')
        function_name = actions.user.formatted_text(text, formatter)
        actions.user.code_insert_function(function_name, None)
