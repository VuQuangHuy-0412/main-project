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
        return self.full_name

