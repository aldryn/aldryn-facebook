# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    """ this migration file was not committed and therefore not included in
    a later release of this package. Noop the migration and reverse eventual
    changes in 0003
    """

    def forwards(self, orm):
        # db.alter_column('cmsplugin_facebookrecommendationbarplugin', 'site', self.gf('django.db.models.fields.CharField')(max_length=100))
        pass

    def backwards(self, orm):
        # db.alter_column('cmsplugin_facebookrecommendationbarplugin', 'site', self.gf('django.db.models.fields.URLField')(max_length=200))
        pass
    
    models = {
        'aldryn_facebook.facebookactivityfeedplugin': {
            'Meta': {'object_name': 'FacebookActivityFeedPlugin', 'db_table': "'cmsplugin_facebookactivityfeedplugin'", '_ormbases': ['cms.CMSPlugin']},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'show_header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_recommendations': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '300'})
        },
        'aldryn_facebook.facebookcommentsplugin': {
            'Meta': {'object_name': 'FacebookCommentsPlugin', 'db_table': "'cmsplugin_facebookcommentsplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'num_posts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'order_by': ('django.db.models.fields.CharField', [], {'default': "'social'", 'max_length': '15'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '450'})
        },
        'aldryn_facebook.facebookfacepileplugin': {
            'Meta': {'object_name': 'FacebookFacepilePlugin', 'db_table': "'cmsplugin_facebookfacepileplugin'", '_ormbases': ['cms.CMSPlugin']},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'num_rows': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'show_count': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'medium'", 'max_length': '6'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '300'})
        },
        'aldryn_facebook.facebookfollowplugin': {
            'Meta': {'object_name': 'FacebookFollowPlugin', 'db_table': "'cmsplugin_facebookfollowplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'layout_style': ('django.db.models.CharField', [], {'default': "'standard'", 'max_length': '20'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '450'})
        },
        'aldryn_facebook.facebooklikeboxplugin': {
            'Meta': {'object_name': 'FacebookLikeBoxPlugin', 'db_table': "'cmsplugin_facebooklikeboxplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'force_wall': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'show_border': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_stream': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '300'})
        },
        'aldryn_facebook.facebooklikeplugin': {
            'Meta': {'object_name': 'FacebookLikePlugin', 'db_table': "'cmsplugin_facebooklikeplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'layout_style': ('django.db.models.CharField', [], {'default': "'standard'", 'max_length': '20'}),
            'ref': ('django.db.models.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'send': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'verb': ('django.db.models.CharField', [], {'default': "'like'", 'max_length': '10'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '450'})
        },
        'aldryn_facebook.facebookrecommendationbarplugin': {
            'Meta': {'object_name': 'FacebookRecommendationBarPlugin', 'db_table': "'cmsplugin_facebookrecommendationbarplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'num_recommendations': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'}),
            'read_time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '30'}),
            'ref': ('django.db.models.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'side': ('django.db.models.fields.CharField', [], {'default': "'right'", 'max_length': '10'}),
            # invalid version: 'site': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'trigger': ('django.db.models.fields.CharField', [], {'default': "'onvisible'", 'max_length': '10'}),
            'verb': ('django.db.models.CharField', [], {'default': "'like'", 'max_length': '10'})
        },
        'aldryn_facebook.facebookrecommendationboxplugin': {
            'Meta': {'object_name': 'FacebookRecommendationBoxPlugin', 'db_table': "'cmsplugin_facebookrecommendationboxplugin'", '_ormbases': ['cms.CMSPlugin']},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'show_header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '300'})
        },
        'aldryn_facebook.facebooksendplugin': {
            'Meta': {'object_name': 'FacebookSendPlugin', 'db_table': "'cmsplugin_facebooksendplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'ref': ('django.db.models.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_facebook']
