class DataMixin:
    def get_user_context(self, **kwargs):
        context = {}
        user = self.request.user
        if user.is_authenticated:
            context['user'] = user
        context.update(kwargs)
        return context
