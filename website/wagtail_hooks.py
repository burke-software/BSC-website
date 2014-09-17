from django.utils.html import format_html, format_html_join
from django.conf import settings

from wagtail.wagtailcore import hooks

@hooks.register('insert_editor_js')
def editor_js():
  js_files = [
    'website/js/hallo-edit-html.js',
  ]
  js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
    ((settings.STATIC_URL, filename) for filename in js_files)
  )
  return js_includes + format_html(
    """
    <script>
        registerHalloPlugin('editHtmlButton');
    </script>
    """
  )

def allow_all_attributes(tag):
    pass

def whitelister_element_rules():
      tags=["a","abbr","acronym","address","area","b","base","bdo","big","blockquote","body","br","button","caption","cite","code","col","colgroup","dd","del","dfn","div","dl","D\
OCTYPE","dt","em","fieldset","form","h1","h2","h3","h4","h5","h6","head","html","hr","i","img","input","ins","kbd","label","legend","li","link","map","meta","noscript","object","\
ol","optgroup","option","p","param","pre","q","samp","script","select","small","span","strong","style","sub","sup","table","tbody","td","textarea","tfoot","th","thead","title","t\
r","tt","ul","var"]
      return dict((tag, allow_all_attributes) for tag in tags)
hooks.register('construct_whitelister_element_rules', whitelister_element_rules)
