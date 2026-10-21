# aggregator_element_start()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.parser.inc`](_file.md), lines 172–215 · [local source](../../../../source/modules/aggregator/aggregator.parser.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc#L172-L215)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_element_start($parser, $name, $attributes)
```

## Documentation

```text
Performs an action when an opening tag is encountered.

Callback function used by xml_parse() within aggregator_parse_feed().
```

## Code

```php
function aggregator_element_start($parser, $name, $attributes) {
  global $item, $element, $tag, $items, $channel;

  $name = strtolower($name);
  switch ($name) {
    case 'image':
    case 'textinput':
    case 'summary':
    case 'tagline':
    case 'subtitle':
    case 'logo':
    case 'info':
      $element = $name;
      break;
    case 'id':
    case 'content':
      if ($element != 'item') {
        $element = $name;
      }
    case 'link':
      // According to RFC 4287, link elements in Atom feeds without a 'rel'
      // attribute should be interpreted as though the relation type is
      // "alternate".
      if (!empty($attributes['HREF']) && (empty($attributes['REL']) || $attributes['REL'] == 'alternate')) {
        if ($element == 'item') {
          $items[$item]['link'] = $attributes['HREF'];
        }
        else {
          $channel['link'] = $attributes['HREF'];
        }
      }
      break;
    case 'item':
      $element = $name;
      $item += 1;
      break;
    case 'entry':
      $element = 'item';
      $item += 1;
      break;
  }

  $tag = $name;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.parser.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
