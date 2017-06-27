from django.contrib import admin
from poll.models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['q_text']}),
        ('Date Information', {'fields': ['q_date'] , 'classes':['collapse']
                              }),
    ]
    inlines = [ChoiceInline]

    list_display = ('q_text', 'q_date', 'published_recently')
    list_filter = ['q_date']

    search_fields = ['q_text', 'choice__c_text']


admin.site.register(Question, QuestionAdmin)
