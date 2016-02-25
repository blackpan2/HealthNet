# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('street', models.CharField(max_length=200)),
                ('zip', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('aptDate', models.DateField()),
                ('aptTime', models.TimeField()),
                ('reason', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('licenseNumber', models.PositiveIntegerField()),
                ('specialty', models.CharField(max_length=200, blank=True)),
                ('addressID', models.ForeignKey(to='base.Address')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('emergencyNumber', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedStay',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('endDate', models.DateField()),
                ('endTime', models.TimeField()),
                ('appointmentID', models.ForeignKey(to='base.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.ForeignKey(to='base.Address', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('policyNumber', models.PositiveIntegerField()),
                ('addressID', models.ForeignKey(to='base.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('extra', models.TextField(blank=True, null=True)),
                ('appt', models.ForeignKey(null=True, blank=True, related_name='+', to='base.Appointment')),
                ('hospital1', models.ForeignKey(null=True, blank=True, related_name='+', to='base.Hospital')),
                ('hospital2', models.ForeignKey(null=True, blank=True, related_name='+', to='base.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('histWeight', models.IntegerField()),
                ('histHeight', models.IntegerField()),
                ('histAge', models.IntegerField()),
                ('histCancer', models.BooleanField()),
                ('histAlcoholism', models.BooleanField()),
                ('histUlcers', models.BooleanField()),
                ('histCholesterol', models.BooleanField()),
                ('histAsthma', models.BooleanField()),
                ('histHeartTrouble', models.BooleanField()),
                ('histKidneyDisease', models.BooleanField()),
                ('histSickleCellAnemia', models.BooleanField()),
                ('histTuberculosis', models.BooleanField()),
                ('histHiv', models.BooleanField()),
                ('histEmphysema', models.BooleanField()),
                ('histHighBloodPressure', models.BooleanField()),
                ('histBleedingDisorder', models.BooleanField()),
                ('histLiverDisorder', models.BooleanField()),
                ('histBirthDefects', models.BooleanField()),
                ('histStroke', models.BooleanField()),
                ('histArthritis', models.BooleanField()),
                ('histDiabetes', models.BooleanField()),
                ('histHeartAttack', models.BooleanField()),
                ('histGout', models.BooleanField()),
                ('histSystems', models.TextField(blank=True)),
                ('histSystemsOther', models.TextField(blank=True)),
                ('histSurgeryTonsils', models.BooleanField()),
                ('histSurgeryBreast', models.BooleanField()),
                ('histSurgeryAppendix', models.BooleanField()),
                ('histSurgeryUterus', models.BooleanField()),
                ('histSurgeryGallBladder', models.BooleanField()),
                ('histSurgeryOvaries', models.BooleanField()),
                ('histSurgeryStomach', models.BooleanField()),
                ('histSurgeryProstate', models.BooleanField()),
                ('histSurgerySmallIntestine', models.BooleanField()),
                ('histSurgeryColon', models.BooleanField()),
                ('histSurgeryThyroid', models.BooleanField()),
                ('histSurgeryKidney', models.BooleanField()),
                ('histSurgeryHernia', models.BooleanField()),
                ('histSurgeryHeart', models.BooleanField()),
                ('histSurgeryPacemaker', models.BooleanField()),
                ('histSurgeryJointReplace', models.BooleanField()),
                ('histSurgeryExtremities', models.BooleanField()),
                ('histSurgeryOther', models.TextField(blank=True)),
                ('histAllergyPenicillin', models.BooleanField()),
                ('histAllergySulfa', models.BooleanField()),
                ('histAllergyMetal', models.BooleanField()),
                ('histAllergyNone', models.BooleanField()),
                ('histAllergyOther', models.TextField(blank=True)),
                ('histAllergyFoodOther', models.TextField(blank=True)),
                ('histMedicationOther', models.TextField(blank=True)),
                ('histConditionShortBreath', models.BooleanField()),
                ('histConditionChestPain', models.BooleanField()),
                ('histConditionWeightLoss', models.BooleanField()),
                ('histConditionConstipation', models.BooleanField()),
                ('histConditionFever', models.BooleanField()),
                ('histConditionVision', models.BooleanField()),
                ('histConditionHeadache', models.BooleanField()),
                ('histConditionUrination', models.BooleanField()),
                ('histConditionNumbness', models.BooleanField()),
                ('histTobaccoCigarettes', models.BooleanField()),
                ('histTobaccoFrequency', models.IntegerField(blank=True)),
                ('histTobaccoDuration', models.IntegerField(blank=True)),
                ('histTobaccoOther', models.TextField(blank=True)),
                ('histAlcoholBeer', models.IntegerField()),
                ('histAlcoholShots', models.IntegerField()),
                ('histDrugOther', models.TextField(blank=True)),
                ('histFamilyCancer', models.BooleanField()),
                ('histFamilyDiabetes', models.BooleanField()),
                ('histFamilyRheumatoidArthritis', models.BooleanField()),
                ('histFamilyArthritis', models.BooleanField()),
                ('histFamilyGout', models.BooleanField()),
                ('histFamilyBleeding', models.BooleanField()),
                ('histFamilySickleCellAnemia', models.BooleanField()),
                ('histFamilyHeartDisease', models.BooleanField()),
                ('histFamilyOther', models.TextField(blank=True)),
                ('histRelationship', models.TextField()),
                ('histWork', models.TextField()),
                ('histWorkExplain', models.TextField(blank=True)),
                ('histPrimaryName', models.TextField()),
                ('histPrimaryNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=120, verbose_name='Subject')),
                ('body', models.CharField(max_length=500, verbose_name='Body')),
                ('sent_at', models.DateTimeField(blank=True, verbose_name='sent at', null=True)),
                ('read_at', models.DateTimeField(blank=True, verbose_name='read at', null=True)),
                ('replied_at', models.DateTimeField(blank=True, verbose_name='replied at', null=True)),
                ('sender_deleted_at', models.DateTimeField(blank=True, verbose_name='Sender deleted at', null=True)),
                ('recipient_deleted_at', models.DateTimeField(blank=True, verbose_name='Recipient deleted at', null=True)),
                ('parent_msg', models.ForeignKey(verbose_name='Parent message', blank=True, null=True, related_name='next_messages', to='base.Message')),
            ],
            options={
                'ordering': ['-sent_at'],
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('license_number', models.PositiveIntegerField()),
                ('department', models.CharField(max_length=300)),
                ('addressID', models.ForeignKey(to='base.Address')),
                ('hospitalID', models.ForeignKey(to='base.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('addressID', models.ForeignKey(to='base.Address')),
                ('emergencyContactID', models.ForeignKey(to='base.EmergencyContact')),
                ('hospitalID', models.ForeignKey(null=True, blank=True, related_name='hospitalID', to='base.Hospital')),
                ('insuranceID', models.ForeignKey(to='base.Insurance')),
                ('medicalID', models.ForeignKey(null=True, blank=True, to='base.MedicalHistory')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ssn', models.PositiveIntegerField()),
                ('birthday', models.DateField()),
                ('phoneNumber', models.PositiveIntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('refill', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('doctorID', models.ForeignKey(to='base.Doctor')),
                ('medication', models.ForeignKey(to='base.Medication')),
                ('patientID', models.ForeignKey(to='base.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Root',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('personID', models.ForeignKey(to='base.Person')),
            ],
        ),
        migrations.CreateModel(
            name='testResults',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('results', models.FileField(upload_to='files', null=True)),
                ('comments', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(to='base.Doctor', related_name='+')),
                ('patient', models.ForeignKey(to='base.Patient', related_name='+')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='personID',
            field=models.ForeignKey(to='base.Person'),
        ),
        migrations.AddField(
            model_name='patient',
            name='preferredHospital',
            field=models.ForeignKey(null=True, blank=True, related_name='preferredHospital', to='base.Hospital'),
        ),
        migrations.AddField(
            model_name='nurse',
            name='personID',
            field=models.ForeignKey(to='base.Person'),
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(verbose_name='Recipient', blank=True, null=True, related_name='received_messages', to='base.Person'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(to='base.Person', verbose_name='Sender', related_name='sent_messages'),
        ),
        migrations.AddField(
            model_name='logger',
            name='medHistory',
            field=models.ForeignKey(null=True, blank=True, related_name='+', to='base.MedicalHistory'),
        ),
        migrations.AddField(
            model_name='logger',
            name='testResults',
            field=models.ForeignKey(null=True, blank=True, related_name='+', to='base.testResults'),
        ),
        migrations.AddField(
            model_name='logger',
            name='user1',
            field=models.ForeignKey(null=True, blank=True, related_name='+', to='base.Person'),
        ),
        migrations.AddField(
            model_name='logger',
            name='user2',
            field=models.ForeignKey(null=True, blank=True, related_name='+', to='base.Person'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='personID',
            field=models.ForeignKey(to='base.Person', null=True, default=None),
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospitalID',
            field=models.ForeignKey(to='base.Hospital'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients',
            field=models.ManyToManyField(to='base.Patient', blank=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='personID',
            field=models.ForeignKey(to='base.Person'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctorID',
            field=models.ForeignKey(to='base.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patientID',
            field=models.ForeignKey(to='base.Patient'),
        ),
        migrations.AddField(
            model_name='admin',
            name='hospitalID',
            field=models.ForeignKey(to='base.Hospital'),
        ),
        migrations.AddField(
            model_name='admin',
            name='personID',
            field=models.ForeignKey(to='base.Person'),
        ),
    ]
