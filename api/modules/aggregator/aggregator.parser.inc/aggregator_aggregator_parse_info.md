# aggregator_aggregator_parse_info()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.parser.inc`](_file.md), lines 11–16 · [local source](../../../../source/modules/aggregator/aggregator.parser.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc#L11-L16)
- **Module/theme:** aggregator
- **Implements:** [hook_aggregator_parse_info()](../aggregator.api.php/hook_aggregator_parse_info.md)

## Signature

```php
function aggregator_aggregator_parse_info()
```

## Documentation

```text
Implements hook_aggregator_parse_info().
```

## Code

```php
function aggregator_aggregator_parse_info() {
  return array(
    'title' => t('Default parser'),
    'description' => t('Parses RSS, Atom and RDF feeds.'),
  );
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.parser.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.parser.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
