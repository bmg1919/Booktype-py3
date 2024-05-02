# -*- coding: utf-8 -*-
import lxml.html
from lxml import etree

from django.db import migrations

from booktype.importer.epub.epubimporter import EpubImporter


def convert_endnotes(apps, schema_editor):
    Chapter = apps.get_model('editor', 'Chapter')

    for chapter in Chapter.objects.all():
        tree = lxml.html.fragment_fromstring(chapter.content, create_parent=True,
                                             parser=lxml.html.HTMLParser(encoding='utf-8'))

        # converting
        tree, _ = EpubImporter.convert_endnotes(tree)

        content = etree.tostring(tree, pretty_print=True, encoding='unicode', xml_declaration=False)

        # remove redundant div wrapper
        a = len("<div>")
        b = content.rfind("</div>")
        chapter.content = content[a:b]

        chapter.save()


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0003_update_books_toc'),
    ]

    operations = [
        migrations.RunPython(convert_endnotes)
    ]
