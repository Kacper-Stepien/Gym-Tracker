from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='exercises/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Plan(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    exercises = models.ManyToManyField(Exercise, blank=True)

    def __str__(self):
        return f"{self.name} (by {self.user.username})"

class WorkoutSession(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.user.username}"
    
class WorkoutSet(models.Model):
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE, related_name="sets")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.FloatField()
    reps = models.IntegerField()

    def __str__(self):
        return f"{self.exercise.name} - {self.weight} kg x {self.reps} reps"
