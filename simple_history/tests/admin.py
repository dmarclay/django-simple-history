from __future__ import unicode_literals

from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin
from .models import (
    Book,
    Choice,
    ConcreteExternal,
    Document,
    Employee,
    FileModel,
    Paper,
    Person,
    Poll
)


class PersonAdmin(SimpleHistoryAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class ChoiceAdmin(SimpleHistoryAdmin):
    history_list_display = ['votes']


class FileModelAdmin(SimpleHistoryAdmin):

    def test_method(self, obj):
        return 'test_method_value'

    history_list_display = ['title', 'test_method']


admin.site.register(Poll, SimpleHistoryAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Book, SimpleHistoryAdmin)
admin.site.register(Document, SimpleHistoryAdmin)
admin.site.register(Paper, SimpleHistoryAdmin)
admin.site.register(Employee, SimpleHistoryAdmin)
admin.site.register(ConcreteExternal, SimpleHistoryAdmin)
admin.site.register(FileModel, FileModelAdmin)
