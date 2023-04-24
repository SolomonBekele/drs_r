from django.db import models
from multiselectfield import MultiSelectField 
from django.core.validators import MaxLengthValidator,MinLengthValidator
# from catboost import CatBoostClassifier
import joblib


GENDER =(
    (0,"Female"),
    (1,"Male"), 
    )

 
class Data(models.Model):
    
    main_features =((0,"high_fever"), (1,"nausea"), (2,"skin_rash"), (3,"yellowish_skin"), 
                    (4,"itching"), (5,"mild_fever"), (6,"vomiting"), (7,"fatigue"),
                    (8,"abnormal_menstruation"),(9,"muscle_weakness"),(10,"indigestion"),
                    (11,"joint_pain"),(12,"yellowing_of_eyes"),(13,"headache"),(14,"blurred_and_distorted_vision"),
                    (15,"continuous_feel_of_urine"),(16,"prominent_veins_on_calf"),(17,"sweating"), 
                    (18,"altered_sensorium"),(19,"lack_of_concentration"), (20,"neck_pain"),
                    (21,"irritation_in_anus"),(22,"abdominal_pain"),(23,"chills"))
    
    name = models.CharField(max_length=100,null=True)
    age = models.PositiveIntegerField()
    sex = models.PositiveIntegerField(choices=main_features,null=True)
    predictions = models.CharField(max_length=100,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def save(self,*arg,**kwargs):
        ml_model = joblib.load("../dr_re/ml_model/ml_model.joblib")  
        self.preditions = ml_model.predict()
        
        return super().save(*arg,**kwargs)
        
    class Meta:
        ordering = ['-date']
    
    def __str__(self) :
        return self.name