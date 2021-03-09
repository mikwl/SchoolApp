from rest_framework import serializers
from .models import School, Group, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('school_name','school_location',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_name','group_facultet','school')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_first_name','student_last_name','student_age','student_group',)


# class PredmetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Predmet
#         field = ('predmet_name')