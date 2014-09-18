"""
This script migrates blog posts from WordPress to Wagtail.
"""

from lxml import etree
from bs4 import BeautifulSoup
from website.models import
from django.template.defaultfilters import slugify
from django.db.utils import IntegrityError
import re

xml_file = 'gkblog/greenkeyresources.wordpress.2014-06-30.xml'
tree = etree.parse(xml_file)
root = tree.getroot()

soup = BeautifulSoup(etree.tostring(root), 'xml')


blog_categories = ['Accounting/Finance', 'Alternative Asset Management', 'Financial Services', 'General Interest',
                       'Green Key In the Community', 'Healthcare', 'HR & Management Tips', 'Human Resources',
                       'Information Technology', 'Job Search Advice', 'Legal', 'New Job Advice', 'Office Support',
                        'Pharmaceutical', 'Temporary Staffing']

for blog_category in blog_categories:
    try:
        BlogCategory.objects.create(name=blog_category, slug=slugify(blog_category))
    except IntegrityError:
        pass

path = 0
for item in soup.findAll('item'):
    if item.find('encoded').string:
        link = item.find('link').string
        if re.findall('\d\d\d\d/\d\d/[^/]+/?$', link):
            link = re.findall('/([^/]+)/?$', link)[0]
        else:
            continue
        body = item.find('encoded').string
        body = '<p> ' + body + ' </p>'
        body = body.replace('\n\n', '</p> <p>')
        #body = body.encode("ascii", "xmlcharrefreplace")
        date = item.find('post_date').string[0:10]
        tags = [tag.string.replace('&amp;', '&') for tag in item.findAll('category', {'domain': 'post_tag'})]
        tag_objects = []
        # Create wagtail tag objects
        for tag in tags:
            try:
                a_tag = Tag.objects.create(name=tag, slug=slugify(tag))
            except IntegrityError:
                a_tag = Tag.objects.get(name=tag)
            tag_objects.append(a_tag)
        title = item.find('title').string
        #title = title.encode("ascii", "xmlcharrefreplace")
        categories = [cat.string.replace('&amp;', '&') for cat in item.findAll('category', {'domain': 'category'})]
        path += 1
        if len(str(path)) == 1:
            the_path = '00010001000{}'.format(str(path))
        if len(str(path)) == 2:
            the_path = '0001000100{}'.format(str(path))
        if len(str(path)) == 3:
            the_path = '000100010{}'.format(str(path))
        if len(str(path)) == 4:
            the_path = '00010001{}'.format(str(path))
        try:
            blog_page = BlogPage.objects.create(body=body, date=date, title=title, depth=3, path=the_path,
                                                    slug=link)
            for category in categories:
                blog_category = BlogCategory.objects.get(name=category)
                blog_page_category = BlogCategoryBlogPage.objects.create(category=blog_category, page=blog_page)
            # Creates blog page tag objects
            for tag in tag_objects:
                blog_tag = BlogPageTag.objects.create(content_object=blog_page, tag=tag)
        except:
            pass











