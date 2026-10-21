# _aggregator_parse_opml()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 383–399 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L383-L399)
- **Module/theme:** aggregator

## Signature

```php
function _aggregator_parse_opml($opml)
```

## Documentation

```text
Parses an OPML file.

Feeds are recognized as <outline> elements with the attributes "text" and
"xmlurl" set.

@param $opml
  The complete contents of an OPML document.

@return
  An array of feeds, each an associative array with a "title" and a "url"
  element, or NULL if the OPML document failed to be parsed. An empty array
  will be returned if the document is valid but contains no feeds, as some
  OPML documents do.
```

## Code

```php
function _aggregator_parse_opml($opml) {
  $feeds = array();
  $xml_parser = drupal_xml_parser_create($opml);
  if (xml_parse_into_struct($xml_parser, $opml, $values)) {
    foreach ($values as $entry) {
      if ($entry['tag'] == 'OUTLINE' && isset($entry['attributes'])) {
        $item = $entry['attributes'];
        if (!empty($item['XMLURL']) && !empty($item['TEXT'])) {
          $feeds[] = array('title' => $item['TEXT'], 'url' => $item['XMLURL']);
        }
      }
    }
  }
  xml_parser_free($xml_parser);

  return $feeds;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
