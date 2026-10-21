# aggregator_element_data()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.parser.inc`](_file.md), lines 246–288 · [local source](../../../../source/modules/aggregator/aggregator.parser.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc#L246-L288)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_element_data($parser, $data)
```

## Documentation

```text
Performs an action when data is encountered.

Callback function used by xml_parse() within aggregator_parse_feed().
```

## Code

```php
function aggregator_element_data($parser, $data) {
  global $channel, $element, $items, $item, $image, $tag;
  $items += array($item => array());
  switch ($element) {
    case 'item':
      $items[$item] += array($tag => '');
      $items[$item][$tag] .= $data;
      break;
    case 'image':
    case 'logo':
      $image += array($tag => '');
      $image[$tag] .= $data;
      break;
    case 'link':
      if ($data) {
        $items[$item] += array($tag => '');
        $items[$item][$tag] .= $data;
      }
      break;
    case 'content':
      $items[$item] += array('content' => '');
      $items[$item]['content'] .= $data;
      break;
    case 'summary':
      $items[$item] += array('summary' => '');
      $items[$item]['summary'] .= $data;
      break;
    case 'tagline':
    case 'subtitle':
      $channel += array('description' => '');
      $channel['description'] .= $data;
      break;
    case 'info':
    case 'id':
    case 'textinput':
      // The sub-element is not supported. However, we must recognize
      // it or its contents will end up in the item array.
      break;
    default:
      $channel += array($tag => '');
      $channel[$tag] .= $data;
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.parser.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
