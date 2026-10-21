# aggregator_element_end()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.parser.inc`](_file.md), lines 222–239 · [local source](../../../../source/modules/aggregator/aggregator.parser.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc#L222-L239)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_element_end($parser, $name)
```

## Documentation

```text
Performs an action when a closing tag is encountered.

Callback function used by xml_parse() within aggregator_parse_feed().
```

## Code

```php
function aggregator_element_end($parser, $name) {
  global $element;

  switch ($name) {
    case 'image':
    case 'textinput':
    case 'item':
    case 'entry':
    case 'info':
      $element = '';
      break;
    case 'id':
    case 'content':
      if ($element == $name) {
        $element = '';
      }
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.parser.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
