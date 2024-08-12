from user.models import User
import django_filters


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Login"
    )

    class Meta:
        model = User
        fields = ['username', 'department', 'building', 'position']
