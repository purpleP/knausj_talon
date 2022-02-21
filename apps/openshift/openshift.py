from talon import Module, Context

mod = Module()
mod.tag("openshift", desc="tag for enabling openshift commands in your terminal")
openshift = "openshift"

ctx = Context()
ctx.matches = r"""
tag: user.openshift
"""

mod.list("openshift_action", desc="actions performed by openshift")
ctx.lists["self.openshift_action"] = ("get", "delete", "describe", "label")

mod.list("openshift_object", desc="objects performed by openshift")
ctx.lists["self.openshift_object"] = (
    "nodes",
    "jobs",
    "pods",
    "namespaces",
    "services",
    "events",
    "deployments",
    "replicasets",
    "daemonsets",
)
