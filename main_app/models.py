from django.db import models

# Create your models here.
class TeacherModel(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id')
    full_name = models.TextField(max_length=100, db_column='full_name')
    rank_and_degree = models.TextField(max_length=50, db_column='rank_and_degree')
    start_time = models.DateField(db_column='start_time')
    birthday = models.DateField(db_column='birthday')
    created_at = models.DateTimeField(db_column='created_at')
    updated_at = models.DateTimeField(db_column='updated_at')

    class Meta:
        db_table = 'teacher'
 
    def __str__(self):
        return self.id

class GroupTeacherModel(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id')
    name = models.TextField(max_length=255, db_column='name')
    description = models.TextField(max_length=1000, db_column='description')
    leader = models.BigIntegerField(db_column='leader')
    created_at = models.DateTimeField(db_column='created_at')
    updated_at = models.DateTimeField(db_column='updated_at')

    class Meta:
        db_table = 'group_teacher'

    def __str__(self):
        return self.id
    
class ClassModel(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id')
    name = models.TextField(max_length=255, db_column='name')
    code = models.TextField(max_length=50, db_column='code', db_collation=ascii)
    semester = models.TextField(max_length=10, db_column='semester')
    subject_id = models.BigIntegerField(db_column='subject_id')
    week = models.TextField(max_length=50, db_column='week')
    day_of_week = models.TextField(max_length=50, db_column='day_of_week')
    time_of_day = models.TextField(max_length=50, db_column='time_of_day')
    is_assigned = models.SmallIntegerField(db_column='is_assigned')
    teacher_id = models.BigIntegerField(db_column='teacher_id')
    created_at = models.DateTimeField(db_column='created_at')
    updated_at = models.DateTimeField(db_column='updated_at')

    class Meta:
        db_table = 'class'
    
    def __str__(self):
        return self.id

class GroupTeacherMappingModel(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id')
    teacher_id = models.BigIntegerField(db_column='teacher_id')
    group_id = models.BigIntegerField(db_column='group_id')
    role = models.TextField(max_length=500, db_column='role')

    class Meta:
        db_table = 'group_teacher_mapping'
    
    def __str__(self):
        return self.id

class LanguageModel(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id')
    name = models.TextField(max_length=100, db_column='name')
    created_at = models.DateTimeField(db_column='created_at')
    updated_at = models.DateTimeField(db_column='updated_at')

    class Meta:
        db_table = 'language'
    
    def __str__(self):
        return self.id

class LanguageTeacherMappingModel(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id')
    teacher_id = models.BigIntegerField(db_column='teacher_id')
    language_id = models.BigIntegerField(db_column='language_id')

    class Meta:
        db_table = 'language_teacher_mapping'
    
    def __str__(self):
        return self.id

class StudentProjectModel(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id')
    name = models.TextField(max_length=100, db_column='name')
    student_code = models.TextField(max_length=50, db_column='student_code')
    class_id = models.BigIntegerField(db_column='class_id')
    is_assigned = models.SmallIntegerField(db_column='is_assigned')
    created_at = models.DateTimeField(db_column='created_at')
    updated_at = models.DateTimeField(db_column='updated_at')
    teacher_1_id = models.BigIntegerField(db_column='teacher_1_id')
    teacher_2_id = models.BigIntegerField(db_column='teacher_2_id')
    teacher_3_id = models.BigIntegerField(db_column='teacher_3_id')
    teacher_assigned_id = models.BigIntegerField(db_column='teacher_assigned_id')

    class Meta:
        db_table = 'student_project'
    
    def __str__(self):
        return self.id

class SubjectModel(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='id')
    name = models.TextField(max_length=255, db_column='name')
    code = models.TextField(max_length=50, db_column='code')
    group_id = models.BigIntegerField(db_column='group_id')
    created_at = models.DateTimeField(db_column='created_at')
    updated_at = models.DateTimeField(db_column='updated_at')

    class Meta:
        db_table = 'subject'
    
    def __str__(self):
        return self.id