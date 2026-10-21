# filter_dom_serialize()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1128–1149 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1128-L1149)
- **Module/theme:** filter

## Signature

```php
function filter_dom_serialize($dom_document)
```

## Documentation

```text
Converts a DOM object back to an HTML snippet.

The function serializes the body part of a DOMDocument back to an XHTML
snippet. The resulting XHTML snippet will be properly formatted to be
compatible with HTML user agents.

@param $dom_document
  A DOMDocument object to serialize, only the tags below
  the first <body> node will be converted.

@return
  A valid (X)HTML snippet, as a string.
```

## Code

```php
function filter_dom_serialize($dom_document) {
  $body_node = $dom_document->getElementsByTagName('body')->item(0);
  $body_content = '';

  if ($body_node !== NULL) {
    foreach ($body_node->getElementsByTagName('script') as $node) {
      filter_dom_serialize_escape_cdata_element($dom_document, $node);
    }

    foreach ($body_node->getElementsByTagName('style') as $node) {
      filter_dom_serialize_escape_cdata_element($dom_document, $node, '/*', '*/');
    }

    foreach ($body_node->childNodes as $child_node) {
      $body_content .= $dom_document->saveXML($child_node);
    }
    return preg_replace('|<([^> ]*)/>|i', '<$1 />', $body_content);
  }
  else {
    return $body_content;
  }
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
