def default_user(backend, user, response, is_new, *args, **kwargs):
    if is_new:
        user.is_staff = True
        user.is_superuser = True
        user.save()
