# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PersonalInfo.email'
        db.alter_column(u'shakti_personalinfo', 'email', self.gf('django.db.models.fields.EmailField')(max_length=30))

    def backwards(self, orm):

        # Changing field 'PersonalInfo.email'
        db.alter_column(u'shakti_personalinfo', 'email', self.gf('django.db.models.fields.EmailField')(max_length=10))

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
            'address': ('django.db.models.fields.TextField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "'testuser@mail.com'", 'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maritial_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'mobile_num': ('django.db.models.fields.CharField', [], {'default': "'+9129089998'", 'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'shakti.qualification': {
            'Meta': {'object_name': 'Qualification'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_degree': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'other_desc': ('django.db.models.fields.TextField', [], {'default': 'None', 'blank': 'True'}),
            'tenth_perc': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'shakti.skills': {
            'Meta': {'object_name': 'Skills'},
            'computer_skills': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projects': ('django.db.models.fields.TextField', [], {}),
            'speciality': ('django.db.models.fields.TextField', [], {})
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