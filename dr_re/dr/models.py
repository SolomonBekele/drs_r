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
    
    main_features =('yellowing_of_eyes', 'itching', 'abdominal_pain', 'joint_pain',
                  'abnormal_menstruation', 'muscle_weakness', 'skin_rash', 'neck_pain',
                   'nausea', 'chills', 'sweating', 'altered_sensorium',
                   'blurred_and_distorted_vision', 'continuous_feel_of_urine', 'yellowish_skin', 'irritation_in_anus',
                   'indigestion', 'prominent_veins_on_calf', 'mild_fever', 'lack_of_concentration')
    
    main_features=()
    name = models.CharField(max_length=100,null=True)
    age = models.PositiveIntegerField(validators=[MinLengthValidator(13),MaxLengthValidator(19)])
    sex = models.PositiveIntegerField(choices=GENDER,null=True)
    predictions = models.CharField(max_length=100,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def save(self,*arg,**kwargs):
        ml_model = joblib.load("dr_re/ml_model/ml_model.joblib")  
        self.preditions = ml_model.predict()
        
        return super().save(*arg,**kwargs)
        
    class Meta:
        ordering = ['-date']
    
    def __str__(self) :
        return self.name