# _batch_current_set()

- **Type:** Function
- **File:** [`includes/batch.inc`](_file.md), lines 377–380 · [local source](../../../source/includes/batch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc#L377-L380)

## Signature

```php
function &_batch_current_set()
```

## Documentation

```text
Returns the batch set being currently processed.
```

## Code

```php
function &_batch_current_set() {
  $batch = &batch_get();
  return $batch['sets'][$batch['current_set']];
}
```

---
_Drupal 7.103 · [includes/batch.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
