# _batch_shutdown()

- **Type:** Function
- **File:** [`includes/batch.inc`](_file.md), lines 490–497 · [local source](../../../source/includes/batch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc#L490-L497)

## Signature

```php
function _batch_shutdown()
```

## Documentation

```text
Shutdown function: Stores the current batch data for the next request.

@see _batch_page()
@see drupal_register_shutdown_function()
```

## Code

```php
function _batch_shutdown() {
  if ($batch = batch_get()) {
    db_update('batch')
      ->fields(array('batch' => serialize($batch)))
      ->condition('bid', $batch['id'])
      ->execute();
  }
}
```

---
_Drupal 7.103 · [includes/batch.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
