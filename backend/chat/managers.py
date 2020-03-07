from django.db import models
from django.db.models import Q


class ThreadQuerySet(models.QuerySet):
    pass


class ThreadManager(models.Manager.from_queryset(ThreadQuerySet)):

    def by_user(self, user):
        qlookup = Q(first=user) | Q(second=user)
        qlookup2 = Q(first=user) & Q(second=user)

        qs = self.get_queryset().filter(qlookup).exclude(qlookup2).distinct()
        return qs

    def get_or_new(self, user, other_username):
        username = user.username
        if username == other_username:
            return None

        qlookup1 = Q(first__username=username) & Q(second__username=other_username)
        qlookup2 = Q(first__username=other_username) & Q(second__username=username)

        qs = self.get_queryset().filter(qlookup1 | qlookup2).distinct()

        if qs.count() == 1:
            return qs.first(), False

        if qs.count() > 1:
            return qs.order_by('timestamp').first(), False

        user2 = user.__class__.objects.get(username=other_username)

        if user is not user2:
            obj = self.model(first=user, second=user2)
            obj.save()
            return obj, True

        return None, False
