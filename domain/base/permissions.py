"""
Plain-function permission checks, for use in services/views where a
class-based mixin doesn't fit (e.g. inside a service function that
needs to check "can this user approve this requisition step").
"""


def can_approve_step(user, step) -> bool:
    profile = getattr(user, "profile", None)
    if profile is None:
        return False
    return step.approver_role == profile.role or (step.is_final and profile.role == "finance")


def is_department_head(user) -> bool:
    profile = getattr(user, "profile", None)
    return bool(profile and profile.role == "hod")
