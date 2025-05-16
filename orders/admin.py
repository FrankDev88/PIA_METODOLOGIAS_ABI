# orders/admin.py
from django.contrib import admin
from .models import Transaction, TransactionItem

class TransactionItemInline(admin.TabularInline):
    model = TransactionItem
    extra = 1  # uno vacío por defecto
    fields = ('food_item', 'quantity', 'subtotal')
    readonly_fields = ('subtotal',)

    def get_readonly_fields(self, request, obj=None):
        # subtotal solo es editable en objetos ya guardados
        if obj:
            return self.readonly_fields
        return ()

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'user__email')
    date_hierarchy = 'created_at'
    inlines = [TransactionItemInline]
    readonly_fields = ('total',)

    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=transactions_report.csv'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Usuario', 'Total', 'Estado', 'Fecha'])

        for obj in queryset:
            writer.writerow([obj.id, obj.user.username, obj.total, obj.status, obj.created_at])

        return response

    export_as_csv.short_description = "Exportar transacciones seleccionadas a CSV"
