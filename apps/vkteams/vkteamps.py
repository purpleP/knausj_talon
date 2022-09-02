from talon import Context, Module, actions

ctx = Context()
mod = Module()
apps = mod.apps
apps.vkteams = "app.name: vkteams"
apps.vkteams = """
os: mac
and app.bundle: ru.mail.messenger-biz-avocado-desktop
"""
