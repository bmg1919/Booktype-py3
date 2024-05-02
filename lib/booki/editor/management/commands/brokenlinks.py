# This file is part of Booktype.
# Copyright (c) 2012 Aleksandar Erkalovic <aleksandar.erkalovic@sourcefabric.org>
#
# Booktype is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Booktype is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Booktype.  If not, see <http://www.gnu.org/licenses/>.

import os
import urllib
from urllib.request import urlopen
from lxml import html

from django.test import Client
from django.core.management.base import BaseCommand, CommandError
from booki.editor import models

cacheLinks = {}


class HeadRequest(urllib.Request):
    def get_method(self):
        return "HEAD"


def checkLink(options, chapter, urlLink):
    global cacheLinks

    if urlLink.startswith("http://"):
        if options['no_remote']:
            return

        for hostUrl in options['ignore_url']:
            if urlLink.startswith(hostUrl):
                return

        print('   >>> ', urlLink)

        if cacheLinks.get(urlLink):
            returnCode = cacheLinks.get(urlLink)
        else:
            try:
                response = urlopen(HeadRequest(urlLink))
            except IOError as e:
                if hasattr(e, 'reason'):
                    returnCode = e.reason
                elif hasattr(e, 'code'):
                    returnCode = e.code
            else:
                returnCode = response.code

            if not options['no_cache']:
                cacheLinks[urlLink] = returnCode

        print('  [%s]' % returnCode)
    else:
        if options['no_local']:
            return

        c = Client()
        newUrl = os.path.normpath('/%s/_v/%s/%s/%s' % (
            chapter.version.book.url_title, chapter.version.getVersion(), chapter.url_title, urlLink))

        print('    >> ', newUrl)
        response = c.get(newUrl)

        print('   [%s]' % response.status_code)


class Command(BaseCommand):
    BOOK_NAMES = '<book name> [, <book name>, ...]'
    help = 'Check links in books.'

    def add_arguments(self, parser):
        parser.add_argument(self.BOOK_NAMES, nargs='+', type=str)

        parser.add_argument('--no-remote',
                            action='store_true',
                            dest='no_remote',
                            default=False,
                            help='Do we check for remote links?')

        parser.add_argument('--no-local',
                            action='store_true',
                            dest='no_local',
                            default=False,
                            help='Do we check for local links?')

        parser.add_argument('--no-cache',
                            action='store_true',
                            dest='no_cache',
                            default=False,
                            help='Do not cache network links.')

        parser.add_argument('--ignore-url',
                            action='append',
                            dest='ignore_url',
                            default=[],
                            help='What hosts to ignore, e.g. http://www.wikipedia.org/')

    def handle(self, *args, **options):
        global cacheLinks

        book_names = options.get(self.BOOK_NAMES, [])

        # filter only books we want
        if book_names:
            booksList = models.Book.objects.filter(url_title__in=book_names).order_by('url_title')
        else:
            booksList = models.Book.objects.all().order_by('url_title')

        for book in booksList:
            print('[%s]' % book.url_title)

            try:
                for chapter in models.Chapter.objects.filter(version__book=book):
                    print('  [%s]' % chapter.url_title)

                    try:
                        tree = html.document_fromstring(chapter.content)
                        print('')
                    except Exception:
                        print('   [ERROR PARSING HTML]')
                        continue

                    for elem in tree.iter():
                        src = elem.get('src')
                        if src:
                            checkLink(options, chapter, src)

                        href = elem.get('href')
                        if href:
                            checkLink(options, chapter, href)
            except Exception:
                pass
