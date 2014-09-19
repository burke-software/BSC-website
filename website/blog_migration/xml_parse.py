"""
This script migrates blog posts from WordPress to Wagtail.
"""

from lxml import etree
from bs4 import BeautifulSoup
from website.models import BlogPage, BlogPageTag, Tag, BlogIndexPage
from django.template.defaultfilters import slugify
from django.db.utils import IntegrityError
import re

xml_file = 'website/blog_migration/technologyagainstyou.wordpress.2014-09-16.xml'
tree = etree.parse(xml_file)
root = tree.getroot()

soup = BeautifulSoup(etree.tostring(root), 'xml')
counter = 0
for item in soup.findAll('item'):
    if item.find('encoded').string:
        link = item.find('link').string
        if re.findall('\d\d\d\d/\d\d/\d\d/[^/]+/?$', link):
            link = re.findall('/([^/]+)/?$', link)[0]
        else:
            continue
        body = item.find('encoded').string
        body = '<p> ' + body + ' </p>'
        body = body.replace('\n\n', '</p> <p>')
        body = body.encode("ascii", "xmlcharrefreplace")
        date = item.find('post_date').string[0:10]
        tags = [tag.string.replace('&amp;', '&') for tag in item.findAll('category', {'domain': 'post_tag'})]
        tag_objects = []
        counter += 1
        if len(str(counter)) == 1:
            the_path = '000100010003000{}'.format(str(counter))
        if len(str(counter)) == 2:
            the_path = '00010001000300{}'.format(str(counter))
        if len(str(counter)) == 3:
            the_path = '0001000100030{}'.format(str(counter))
        if len(str(counter)) == 4:
            the_path = '000100010003{}'.format(str(counter))
        # Create wagtail tag objects
        for tag in tags:
            try:
                a_tag = Tag.objects.create(name=tag, slug=slugify(tag))
            except IntegrityError:
                a_tag = Tag.objects.get(name=tag)
            tag_objects.append(a_tag)
        title = item.find('title').string
        popular_post_dates = ['2012-04-26', '2011-08-10', '2013-08-20', '2013-04-21', '2010-09-16', '2010-01-12',
                              '2010-10-17']
        try:
            if date[3] == '3' or date[3] == '4' or date in popular_post_dates:
                print date
                blog_page = BlogPage.objects.create(body=body, date=date, title=title, depth=4, path=the_path,
                                                    slug=link)

                # Creates blog page tag objects
                for tag in tag_objects:
                    blog_tag = BlogPageTag.objects.create(content_object=blog_page, tag=tag)
        except IntegrityError:
            pass















