# _aggregator_has_categories()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 288–290 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L288-L290)
- **Module/theme:** aggregator

## Signature

```php
function _aggregator_has_categories()
```

## Documentation

```text
Determines whether there are any aggregator categories.

@return
  TRUE if there is at least one category and the user has access to them;
  FALSE otherwise.
```

## Code

```php
function _aggregator_has_categories() {
  return user_access('access news feeds') && (bool) db_query_range('SELECT 1 FROM {aggregator_category}', 0, 1)->fetchField();
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
