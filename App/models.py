from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Department(models.Model):
    dep_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # FK to User model
    dep = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[("Active", "Active"), ("Inactive", "Inactive")])


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.role}"


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)  # FK to Employee model
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("Present", "Present"), ("Absent", "Absent")])

    def __str__(self):
        return f"{self.emp.user.username} - {self.date} - {self.status}"


class Leaves(models.Model):
    leave_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)  # FK to Employee model
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"Leave Request by {self.emp.user.username} from {self.start_date} to {self.end_date}"


class Apology(models.Model):
    apology_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)  # FK to Employee model
    date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"Apology by {self.emp.user.username} on {self.date}"


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # FK to User model
    date = models.DateField()

    def __str__(self):
        return f"Report by {self.user.username} on {self.date}"
