from rest_framework import serializers
from . import models

"""
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('id','email','name','interestlevel',''address','useremail','created','updated')
"""

class PatientSerializer(serializers.ModelSerializer):
    # username = serializers.SlugRelatedField(slug_field=models.User.USERNAME_FIELD,required=False, allow_null=True, queryset=models.User.objects.all(), source='user')
    # first_name = serializers.CharField(source='user.first_name')
    # last_name = serializers.CharField(source='user.last_name')
    # email = serializers.CharField(source='user.email')
    class Meta:
        model = models.Patient
        fields = ('address', 'contact',)#'user','username', 'first_name', 'last_name', 'email')

# assigned = serializers.SlugRelatedField(
#         slug_field=User.USERNAME_FIELD, required=False, allow_null=True,
#         queryset=User.objects.all())
#     status_display = serializers.SerializerMethodField()
#     links = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Task
#         fields = ('id', 'name', 'description', 'sprint', 'status',
#             'status_display', 'order', 'assigned', 'started', 'due',
#             'completed', 'links', )
#
#     def get_status_display(self, obj):
#         return obj.get_status_display()
#
#     def get_links(self, obj):
#         request = self.context['request']
#         links = {
#             'self': reverse('task-detail',
#                 kwargs={'pk': obj.pk}, request=request),
#             'sprint': None,
#             'assigned': None
#         }
#         if obj.sprint_id:
#             links['sprint'] = reverse('sprint-detail',
#                 kwargs={'pk': obj.sprint_id}, request=request)
#         if obj.assigned:
#             links['assigned'] = reverse('user-detail',
#                 kwargs={User.USERNAME_FIELD: obj.assigned}, request=request)
#         return links
#
#     def validate_sprint(self, value):
#         if self.instance and self.instance.pk:
#             if value != self.instance.sprint:
#                 if self.instance.status == Task.STATUS_DONE:
#                     msg = _('Cannot change the sprint of a completed task.')
#                     raise serializers.ValidationError(msg)
#                 if value and value.end < date.today():
#                     msg = _('Cannot assign tasks to past sprints.')
#                     raise serializers.ValidationError(msg)
#         else:
#             if value and value.end < date.today():
#                 msg = _('Cannot add tasks to past sprints.')
#                 raise serializers.ValidationError(msg)
#         return value
#
#     def validate(self, attrs):
#         sprint = attrs.get('sprint')
#         status = attrs.get('status', Task.STATUS_TODO)
#         started = attrs.get('started')
#         completed = attrs.get('completed')
#         if not sprint and status != Task.STATUS_TODO:
#             msg = _('Backlog tasks must have "Not Started" status.')
#             raise serializers.ValidationError(msg)
#         if started and status == Task.STATUS_TODO:
#             msg = _('Started date cannot be set for not started tasks.')
#             raise serializers.ValidationError(msg)
#         if completed and status != Task.STATUS_DONE:
#             msg = _('Completed date cannot be set for uncompleted tasks.')
#             raise serializers.ValidationError(msg)
#         return attrs
