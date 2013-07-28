# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PersonalInfo'
        db.create_table(u'shakti_personalinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(default='testuser@mail.com', max_length=30)),
            ('mobile_num', self.gf('django.db.models.fields.CharField')(default='+9129089998', max_length=15)),
            ('maritial_status', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'shakti', ['PersonalInfo'])

        # Adding model 'Tracker'
        db.create_table(u'shakti_tracker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shakti.PersonalInfo'])),
            ('placed', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('details', self.gf('django.db.models.fields.CharField')(default=None, max_length=10)),
            ('doj', self.gf('django.db.models.fields.DateField')(default=None)),
        ))
        db.send_create_signal(u'shakti', ['Tracker'])

        # Adding model 'Skills'
        db.create_table(u'shakti_skills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shakti.PersonalInfo'])),
            ('projects', self.gf('django.db.models.fields.TextField')()),
            ('computer_skills', self.gf('django.db.models.fields.TextField')()),
            ('speciality', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'shakti', ['Skills'])

        # Adding model 'Qualification'
        db.create_table(u'shakti_qualification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shakti.PersonalInfo'])),
            ('tenth_perc', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('latest_degree', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('other_desc', self.gf('django.db.models.fields.TextField')(default=None, blank=True)),
        ))
        db.send_create_signal(u'shakti', ['Qualification'])

        # Adding model 'Constraints'
        db.create_table(u'shakti_constraints', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shakti.PersonalInfo'])),
            ('night_shift', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('relocatable', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('special_assistance', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('assistance_descr', self.gf('django.db.models.fields.CharField')(default=None, max_length=200)),
        ))
        db.send_create_signal(u'shakti', ['Constraints'])

        # Adding model 'Orthopedic'
        db.create_table(u'shakti_orthopedic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shakti.PersonalInfo'])),
            ('rleg_amputee', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('lleg_amputee', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rhand_amputee', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('lhand_amputee', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('orthopedic_aid', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'shakti', ['Orthopedic'])

        # Adding model 'Vision'
        db.create_table(u'shakti_vision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shakti.PersonalInfo'])),
            ('severity', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'shakti', ['Vision'])

        # Adding model 'Hearing'
        db.create_table(u'shakti_hearing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shakti.PersonalInfo'])),
            ('hearing_aid', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'shakti', ['Hearing'])

        # Adding model 'Other'
        db.create_table(u'shakti_other', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shakti.PersonalInfo'])),
            ('other_description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'shakti', ['Other'])

        # Adding model 'JobDescriptor'
        db.create_table(u'shakti_jobdescriptor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('qualification', self.gf('django.db.models.fields.TextField')()),
            ('who_can', self.gf('django.db.models.fields.TextField')(max_length=20)),
            ('night_shift', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('skills_required', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'shakti', ['JobDescriptor'])


    def backwards(self, orm):
        # Deleting model 'PersonalInfo'
        db.delete_table(u'shakti_personalinfo')

        # Deleting model 'Tracker'
        db.delete_table(u'shakti_tracker')

        # Deleting model 'Skills'
        db.delete_table(u'shakti_skills')

        # Deleting model 'Qualification'
        db.delete_table(u'shakti_qualification')

        # Deleting model 'Constraints'
        db.delete_table(u'shakti_constraints')

        # Deleting model 'Orthopedic'
        db.delete_table(u'shakti_orthopedic')

        # Deleting model 'Vision'
        db.delete_table(u'shakti_vision')

        # Deleting model 'Hearing'
        db.delete_table(u'shakti_hearing')

        # Deleting model 'Other'
        db.delete_table(u'shakti_other')

        # Deleting model 'JobDescriptor'
        db.delete_table(u'shakti_jobdescriptor')


    models = {
        u'shakti.constraints': {
            'Meta': {'object_name': 'Constraints'},
            'assistance_descr': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'night_shift': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'relocatable': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'special_assistance': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'uid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shakti.PersonalInfo']"})
        },
        u'shakti.hearing': {
            'Meta': {'object_name': 'Hearing'},
            'hearing_aid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shakti.PersonalInfo']"})
        },
        u'shakti.jobdescriptor': {
            'Meta': {'object_name': 'JobDescriptor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'night_shift': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'post': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'qualification': ('django.db.models.fields.TextField', [], {}),
            'skills_required': ('django.db.models.fields.TextField', [], {}),
            'who_can': ('django.db.models.fields.TextField', [], {'max_length': '20'})
        },
        u'shakti.orthopedic': {
            'Meta': {'object_name': 'Orthopedic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lhand_amputee': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'lleg_amputee': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'orthopedic_aid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rhand_amputee': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rleg_amputee': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shakti.PersonalInfo']"})
        },
        u'shakti.other': {
            'Meta': {'object_name': 'Other'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_description': ('django.db.models.fields.TextField', [], {}),
            'uid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shakti.PersonalInfo']"})
        },
        u'shakti.personalinfo': {
            'Meta': {'object_name': 'PersonalInfo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "'testuser@mail.com'", 'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'maritial_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'mobile_num': ('django.db.models.fields.CharField', [], {'default': "'+9129089998'", 'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'shakti.qualification': {
            'Meta': {'object_name': 'Qualification'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_degree': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'other_desc': ('django.db.models.fields.TextField', [], {'default': 'None', 'blank': 'True'}),
            'tenth_perc': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shakti.PersonalInfo']"})
        },
        u'shakti.skills': {
            'Meta': {'object_name': 'Skills'},
            'computer_skills': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projects': ('django.db.models.fields.TextField', [], {}),
            'speciality': ('django.db.models.fields.TextField', [], {}),
            'uid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shakti.PersonalInfo']"})
        },
        u'shakti.tracker': {
            'Meta': {'object_name': 'Tracker'},
            'details': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10'}),
            'doj': ('django.db.models.fields.DateField', [], {'default': 'None'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'placed': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shakti.PersonalInfo']"})
        },
        u'shakti.vision': {
            'Meta': {'object_name': 'Vision'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'uid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shakti.PersonalInfo']"})
        }
    }

    complete_apps = ['shakti']