###############################################################################
#                         Models for the ez_main app                          #
###############################################################################

from django.db import models
from users.models import *

class Classes_list(models.Model):
   """ Complete list of all classes """
   class_name      = models.CharField(max_length=200)
   major           = models.CharField(max_length=100)
   class_extension = models.CharField(max_length=200)
   credit          = models.IntegerField(default=25)

   def __str__(self):
      """ Returning a string representation of the model """
      return self.class_name

   def display_classes(self, class1, class2, class3, class4, class5, class6):
      """ Get information for each class in a users class schedule """
      info1 = Classes_list.objects.raw("select id, credit from main_db.ez_main_classes_list where class_name = %s limit 1", [class1]) 
      info2 = Classes_list.objects.raw("select id, credit from main_db.ez_main_classes_list where class_name = %s limit 1", [class2])
      info3 = Classes_list.objects.raw("select id, credit from main_db.ez_main_classes_list where class_name = %s limit 1", [class3])
      info4 = Classes_list.objects.raw("select id, credit from main_db.ez_main_classes_list where class_name = %s limit 1", [class4])
      info5 = Classes_list.objects.raw("select id, credit from main_db.ez_main_classes_list where class_name = %s limit 1", [class5])
      info6 = Classes_list.objects.raw("select id, credit from main_db.ez_main_classes_list where class_name = %s limit 1", [class6])

      return info1[0], info2[0], info3[0], info4[0], info5[0], info6[0]

class Class_schedule(models.Model):
   """ Class schedule associated with each user """
   user_id = models.OneToOneField(User_profile ,on_delete=models.CASCADE, primary_key=True)
   class1  = models.CharField(max_length = 200,  null = True, blank = True)
   class2  = models.CharField(max_length = 200,  null = True, blank = True)
   class3  = models.CharField(max_length = 200,  null = True, blank = True)
   class4  = models.CharField(max_length = 200,  null = True, blank = True)
   class5  = models.CharField(max_length = 200,  null = True, blank = True)
   class6  = models.CharField(max_length = 200,  null = True, blank = True)

   def __str__(self):
      """ Returning a string representation of the model """
      return self.class1 + " - " + self.class2 + " - " + self.class3 + " - " + self.class4 + " - " + self.class5 + " - " + self.class6

   def create_class(self, major):
      """ Create a randomized class schedule based on major linked to a user """
      query_major = major
      random_classes = Classes_list.objects.raw("select id, class_name from main_db.ez_main_classes_list where major = %s order by rand() limit 6", [query_major])
      self.class1 = str(random_classes[0])
      self.class2 = str(random_classes[1])
      self.class3 = str(random_classes[2])
      self.class4 = str(random_classes[3])
      self.class5 = str(random_classes[4])
      self.class6 = str(random_classes[5])

      return random_classes