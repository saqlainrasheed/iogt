# Generated by Django 3.1.14 on 2022-01-06 09:08

from django.db import migrations
import home.blocks
import messaging.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_localedetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title', template='blocks/heading.html')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image'])), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('paragraph_v1_legacy', home.blocks.RawHTMLBlock(icon='code')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list', wagtail.core.blocks.ListBlock(wagtailmarkdown.blocks.MarkdownBlock(icon='code'))), ('numbered_list', home.blocks.NumberedListBlock(wagtailmarkdown.blocks.MarkdownBlock(icon='code'))), ('page_button', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('embedded_poll', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('poll', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Poll']))])), ('embedded_survey', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('survey', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Survey']))])), ('embedded_quiz', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('quiz', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Quiz']))])), ('media', home.blocks.MediaBlock(icon='media')), ('chat_bot', wagtail.core.blocks.StructBlock([('subject', wagtail.core.blocks.CharBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('trigger_string', wagtail.core.blocks.CharBlock()), ('channel', messaging.blocks.ChatBotChannelChooserBlock())]))]),
        ),
        migrations.AlterField(
            model_name='offlineapppage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title', template='blocks/heading.html')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image'])), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('paragraph_v1_legacy', home.blocks.RawHTMLBlock(icon='code')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list', wagtail.core.blocks.ListBlock(wagtailmarkdown.blocks.MarkdownBlock(icon='code'))), ('numbered_list', home.blocks.NumberedListBlock(wagtailmarkdown.blocks.MarkdownBlock(icon='code'))), ('page_button', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('embedded_poll', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('poll', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Poll']))])), ('embedded_survey', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('survey', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Survey']))])), ('embedded_quiz', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('quiz', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Quiz']))])), ('media', home.blocks.MediaBlock(icon='media')), ('chat_bot', wagtail.core.blocks.StructBlock([('subject', wagtail.core.blocks.CharBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('trigger_string', wagtail.core.blocks.CharBlock()), ('channel', messaging.blocks.ChatBotChannelChooserBlock())])), ('offline_app_button', wagtail.core.blocks.StructBlock([('smartphone_text', wagtail.core.blocks.CharBlock(help_text='This text appears when it is possible for the user to install the app on their phone.')), ('feature_phone_text', wagtail.core.blocks.CharBlock(help_text='This text appears when the user is using a feature phone and thus cannot install the app (the button will be disabled in this case). [Currently not implemented]', required=False)), ('offline_text', wagtail.core.blocks.CharBlock(help_text="This text appears when the user is navigating the site via the offline app and thus it doesn't make sense to install the offline app again (the button will be disabled in this case). [Currently not implemented]", required=False))]))]),
        ),
    ]
