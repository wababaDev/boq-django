"""
Cross-cutting middleware. Keep anything request-lifecycle related here
rather than bolting it onto individual views.
"""


class AuditLogMiddleware:
    """Placeholder — wire up real audit logging once the loan domain exists."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
