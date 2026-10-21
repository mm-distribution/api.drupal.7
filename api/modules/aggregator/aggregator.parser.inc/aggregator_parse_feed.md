# aggregator_parse_feed()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.parser.inc`](_file.md), lines 67–165 · [local source](../../../../source/modules/aggregator/aggregator.parser.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc#L67-L165)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_parse_feed(&$data, $feed)
```

## Documentation

```text
Parses a feed and stores its items.

@param $data
  The feed data.
@param $feed
  An object describing the feed to be parsed.

@return
  FALSE on error, TRUE otherwise.
```

## Code

```php
function aggregator_parse_feed(&$data, $feed) {
  global $items, $image, $channel;

  // Unset the global variables before we use them.
  unset($GLOBALS['element'], $GLOBALS['item'], $GLOBALS['tag']);
  $items = array();
  $image = array();
  $channel = array();

  // Parse the data.
  $xml_parser = drupal_xml_parser_create($data);
  xml_set_element_handler($xml_parser, 'aggregator_element_start', 'aggregator_element_end');
  xml_set_character_data_handler($xml_parser, 'aggregator_element_data');

  if (!xml_parse($xml_parser, $data, 1)) {
    watchdog('aggregator', 'The feed from %site seems to be broken, due to an error "%error" on line %line.', array('%site' => $feed->title, '%error' => xml_error_string(xml_get_error_code($xml_parser)), '%line' => xml_get_current_line_number($xml_parser)), WATCHDOG_WARNING);
    drupal_set_message(t('The feed from %site seems to be broken, because of error "%error" on line %line.', array('%site' => $feed->title, '%error' => xml_error_string(xml_get_error_code($xml_parser)), '%line' => xml_get_current_line_number($xml_parser))), 'error');
    return FALSE;
  }
  xml_parser_free($xml_parser);

  // We reverse the array such that we store the first item last, and the last
  // item first. In the database, the newest item should be at the top.
  $items = array_reverse($items);

  // Initialize items array.
  $feed->items = array();
  foreach ($items as $item) {

    // Prepare the item:
    foreach ($item as $key => $value) {
      $item[$key] = trim($value);
    }

    // Resolve the item's title. If no title is found, we use up to 255
    // characters of the description ending at a word boundary.
    if (!empty($item['title'])) {
      $item['title'] = $item['title'];
    }
    elseif (!empty($item['description'])) {
      $clean_description = strip_tags(html_entity_decode($item['description'], ENT_QUOTES, 'UTF-8'));
      $item['title'] = truncate_utf8($clean_description, 255, TRUE, TRUE);
    }
    else {
      $item['title'] = '';
    }

    // Resolve the items link.
    if (!empty($item['link'])) {
      $item['link'] = $item['link'];
    }
    else {
      $item['link'] = $feed->link;
    }

    // Atom feeds have an ID tag instead of a GUID tag.
    if (!isset($item['guid'])) {
      $item['guid'] = isset($item['id']) ? $item['id'] : '';
    }

    // Atom feeds have a content and/or summary tag instead of a description tag.
    if (!empty($item['content:encoded'])) {
      $item['description'] = $item['content:encoded'];
    }
    elseif (!empty($item['summary'])) {
      $item['description'] = $item['summary'];
    }
    elseif (!empty($item['content'])) {
      $item['description'] = $item['content'];
    }

    // Try to resolve and parse the item's publication date.
    $date = '';
    foreach (array('pubdate', 'dc:date', 'dcterms:issued', 'dcterms:created', 'dcterms:modified', 'issued', 'created', 'modified', 'published', 'updated') as $key) {
      if (!empty($item[$key])) {
        $date = $item[$key];
        break;
      }
    }

    $item['timestamp'] = strtotime($date);

    if ($item['timestamp'] === FALSE) {
      $item['timestamp'] = aggregator_parse_w3cdtf($date); // Aggregator_parse_w3cdtf() returns FALSE on failure.
    }

    // Resolve dc:creator tag as the item author if author tag is not set.
    if (empty($item['author']) && !empty($item['dc:creator'])) {
      $item['author'] = $item['dc:creator'];
    }

    $item += array('author' => '', 'description' => '');

    // Store on $feed object. This is where processors will look for parsed items.
    $feed->items[] = $item;
  }

  return TRUE;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.parser.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
