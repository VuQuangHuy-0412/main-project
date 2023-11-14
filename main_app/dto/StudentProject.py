class StudentProject:
    def __init__(self, id, name, student_code, class_id, is_assigned, created_at, updated_at, teacher_1_id, teacher_2_id, teacher_3_id, teacher_assigned_id):
        self.id = id
        self.name = name
        self.student_code = student_code
        self.class_id = class_id
        self.is_assigned = is_assigned
        self.created_at = created_at
        self.updated_at = updated_at
        self.teacher_1_id = teacher_1_id
        self.teacher_2_id = teacher_2_id
        self.teacher_3_id = teacher_3_id
        self.teacher_assigned_id = teacher_assigned_id