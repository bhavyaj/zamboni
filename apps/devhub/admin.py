from django.contrib import admin

from .models import HubPromo, HubEvent, ActivityLog


class HubPromoAdmin(admin.ModelAdmin):
    list_display = ('heading', 'body', 'visibility')
    list_editable = ('visibility',)


class HubEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'location', 'date')


class HubNewsAdmin(admin.ModelAdmin):
    list_display = ('created', 'user', 'action', 'arguments')
    raw_id_fields = ('user',)
    list_filter = ('action',)
    readonly_fields = ('created', 'user', 'action', '_arguments', '_details')
    date_hierarchy = 'created'
    raw_id_fields = ('user',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(HubPromo, HubPromoAdmin)
admin.site.register(HubEvent, HubEventAdmin)
admin.site.register(ActivityLog, HubNewsAdmin)
