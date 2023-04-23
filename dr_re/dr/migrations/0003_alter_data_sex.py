# Generated by Django 4.2 on 2023-04-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0002_alter_data_options_data_date_data_predictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='sex',
            field=models.PositiveIntegerField(choices=[(0, 'high_fever'), (1, 'nausea'), (2, 'skin_rash'), (3, 'yellowish_skin'), (4, 'itching'), (5, 'mild_fever'), (6, 'vomiting'), (7, 'fatigue'), (8, 'abnormal_menstruation'), (9, 'muscle_weakness'), (10, 'indigestion'), (11, 'joint_pain'), (12, 'yellowing_of_eyes'), (13, 'headache'), (14, 'blurred_and_distorted_vision'), (15, 'continuous_feel_of_urine'), (16, 'prominent_veins_on_calf'), (17, 'sweating'), (18, 'altered_sensorium'), (19, 'lack_of_concentration'), (20, 'neck_pain'), (21, 'irritation_in_anus'), (22, 'abdominal_pain'), (23, 'chills')], null=True),
        ),
    ]