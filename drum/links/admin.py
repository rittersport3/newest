from __future__ import unicode_literals

from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin
from drum.links.models import Link


class LinkAdmin(DisplayableAdmin):

    list_display = ("id", "title", "link", "status", "publish_date",
                    "user", "comments_count", "rating_sum")
    list_display_links = ("id",)
    list_editable = ("title", "link", "status")
    list_filter = ("status", "user__username")
    search_fields = ("title", "link", "user__username", "user__email")
    ordering = ("-publish_date",)

    fieldsets = (
        (None, {
            "fields": ("title", "link", "status", "publish_date", "user"),
        }),
    )


admin.site.register(Link, LinkAdmin)
