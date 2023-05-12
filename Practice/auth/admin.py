from django.contrib import admin
import django.contrib
import auth.models




# @admin.register(auth.models.auth)
# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         auth.models.auth.name.field.name,
#         auth.models.auth.mail.field.name,
#         auth.models.auth.feedback_text.field.name,
#     )
#     fields = (
#         auth.models.Feedback.name.field.name,
#         feedback.models.Feedback.mail.field.name,
#         feedback.models.Feedback.feedback_text.field.name,
#         # feedback.models.Feedback.created_on.field.name