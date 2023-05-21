from django.db import models
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
    symptom =["high_fever","nausea","skin_rash","yellowish_skin",
                    "itching","mild_fever","vomiting","fatigue",
                    "abnormal_menstruation","muscle_weakness","indigestion",
                    "joint_pain","yellowing_of_eyes","headache","blurred_and_distorted_vision",
                    "continuous_feel_of_urine","prominent_veins_on_calf","sweating", 
                    "altered_sensorium","lack_of_concentration","neck_pain"
                    ,"irritation_in_anus","abdominal_pain","chills"]
    l=[0]*24
    ll={0: '(vertigo) Paroymsal  Positional Vertigo',1: 'AIDS',2: 'Acne',3: 'Alcoholic hepatitis',4: 'Allergy',5: 'Arthritis',
         6: 'Bronchial Asthma',7: 'Cervical spondylosis',8: 'Chicken pox',9: 'Chronic cholestasis',10: 'Common Cold',
         11: 'Dengue',12: 'Diabetes ',13: 'Dimorphic hemmorhoids(piles)',14: 'Drug Reaction',15: 'Fungal infection',
         16: 'GERD',17: 'Gastroenteritis',18: 'Heart attack',19: 'Hepatitis B',20: 'Hepatitis C',21: 'Hepatitis D',
         22: 'Hepatitis E',23: 'Hypertension ',24: 'Hyperthyroidism',25: 'Hypoglycemia',26: 'Hypothyroidism',27: 'Impetigo',
         28: 'Jaundice',29: 'Malaria',30: 'Migraine',31: 'Osteoarthristis',32: 'Paralysis (brain hemorrhage)',33: 'Peptic ulcer diseae',
         34: 'Pneumonia',35: 'Psoriasis',36: 'Tuberculosis',37: 'Typhoid',38: 'Urinary tract infection',39: 'Varicose veins',
         40: 'hepatitis A'}
    
    def save(self,*arg,**kwargs):
      
        
        return super().save(*arg,**kwargs)
        
    
    def __str__(self) :
        return self.name