# _batch_next_set()

- **Type:** Function
- **File:** [`includes/batch.inc`](_file.md), lines 392–404 · [local source](../../../source/includes/batch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc#L392-L404)

## Signature

```php
function _batch_next_set()
```

## Documentation

```text
Retrieves the next set in a batch.

If there is a subsequent set in this batch, assign it as the new set to
process and execute its form submit handler (if defined), which may add
further sets to this batch.

@return
  TRUE if a subsequent set was found in the batch.
```

## Code

```php
function _batch_next_set() {
  $batch = &batch_get();
  if (isset($batch['sets'][$batch['current_set'] + 1])) {
    $batch['current_set']++;
    $current_set = &_batch_current_set();
    if (isset($current_set['form_submit']) && ($function = $current_set['form_submit']) && function_exists($function)) {
      // We use our stored copies of $form and $form_state to account for
      // possible alterations by previous form submit handlers.
      $function($batch['form_state']['complete form'], $batch['form_state']);
    }
    return TRUE;
  }
}
```

---
_Drupal 7.103 · [includes/batch.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
