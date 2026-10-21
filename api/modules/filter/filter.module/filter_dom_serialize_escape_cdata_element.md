# filter_dom_serialize_escape_cdata_element()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1172–1191 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1172-L1191)
- **Module/theme:** filter

## Signature

```php
function filter_dom_serialize_escape_cdata_element($dom_document, $dom_element, $comment_start = '//', $comment_end = '')
```

## Documentation

```text
Adds comments around the <!CDATA section in a dom element.

DOMDocument::loadHTML in filter_dom_load() makes CDATA sections from the
contents of inline script and style tags.  This can cause HTML 4 browsers to
throw exceptions.

This function attempts to solve the problem by creating a DocumentFragment
and imitating the behavior in drupal_get_js(), commenting the CDATA tag.

@param $dom_document
  The DOMDocument containing the $dom_element.
@param $dom_element
  The element potentially containing a CDATA node.
@param $comment_start
  (optional) A string to use as a comment start marker to escape the CDATA
  declaration. Defaults to '//'.
@param $comment_end
  (optional) A string to use as a comment end marker to escape the CDATA
  declaration. Defaults to an empty string.
```

## Code

```php
function filter_dom_serialize_escape_cdata_element($dom_document, $dom_element, $comment_start = '//', $comment_end = '') {
  foreach ($dom_element->childNodes as $node) {
    if (get_class($node) == 'DOMCdataSection') {
      // See drupal_get_js().  This code is more or less duplicated there.
      $embed_prefix = "\n<!--{$comment_start}--><![CDATA[{$comment_start} ><!--{$comment_end}\n";
      $embed_suffix = "\n{$comment_start}--><!]]>{$comment_end}\n";

      // Prevent invalid cdata escaping as this would throw a DOM error.
      // This is the same behavior as found in libxml2.
      // Related W3C standard: http://www.w3.org/TR/REC-xml/#dt-cdsection
      // Fix explanation: http://en.wikipedia.org/wiki/CDATA#Nesting
      $data = str_replace(']]>', ']]]]><![CDATA[>', $node->data);

      $fragment = $dom_document->createDocumentFragment();
      $fragment->appendXML($embed_prefix . $data . $embed_suffix);
      $dom_element->appendChild($fragment);
      $dom_element->removeChild($node);
    }
  }
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
