# _aggregator_items()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 788–790 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L788-L790)
- **Module/theme:** aggregator

## Signature

```php
function _aggregator_items($count)
```

## Documentation

```text
Helper function for drupal_map_assoc.

@param $count
  Items count.

@return
  A string that is plural-formatted as "@count items".
```

## Code

```php
function _aggregator_items($count) {
  return format_plural($count, '1 item', '@count items');
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
