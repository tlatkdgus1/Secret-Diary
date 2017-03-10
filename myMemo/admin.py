from django.contrib import admin
from .models import MyUser
from .models import PublicMemo
from .models import PrivateMemo


admin.site.register(MyUser)
admin.site.register(PublicMemo)
admin.site.register(PrivateMemo)