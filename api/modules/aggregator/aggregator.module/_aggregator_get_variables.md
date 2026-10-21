# _aggregator_get_variables()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 597–612 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L597-L612)
- **Module/theme:** aggregator

## Signature

```php
function _aggregator_get_variables()
```

## Documentation

```text
Gets the fetcher, parser, and processors.

@return
  An array containing the fetcher, parser, and processors.
```

## Code

```php
function _aggregator_get_variables() {
  // Fetch the feed.
  $fetcher = variable_get('aggregator_fetcher', 'aggregator');
  if ($fetcher == 'aggregator') {
    include_once DRUPAL_ROOT . '/' . drupal_get_path('module', 'aggregator') . '/aggregator.fetcher.inc';
  }
  $parser = variable_get('aggregator_parser', 'aggregator');
  if ($parser == 'aggregator') {
    include_once DRUPAL_ROOT . '/' . drupal_get_path('module', 'aggregator') . '/aggregator.parser.inc';
  }
  $processors = variable_get('aggregator_processors', array('aggregator'));
  if (in_array('aggregator', $processors)) {
    include_once DRUPAL_ROOT . '/' . drupal_get_path('module', 'aggregator') . '/aggregator.processor.inc';
  }
  return array($fetcher, $parser, $processors);
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
