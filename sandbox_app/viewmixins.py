class AuthorRequiredMixin(object):
    """
    Authors may edit or delete their own posts only.
    """

    def get_queryset(self):
        queryset = super(AuthorRequiredMixin, self).get_queryset()
        return queryset.filter(author=self.request.user)
