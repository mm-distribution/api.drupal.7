# batch_get()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4787–4796 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4787-L4796)
- **Topics:** [batch](../../topics/batch.md)

## Signature

```php
function &batch_get()
```

## Documentation

```text
Retrieves the current batch.
```

## Code

```php
function &batch_get() {
  // Not drupal_static(), because Batch API operates at a lower level than most
  // use-cases for resetting static variables, and we specifically do not want a
  // global drupal_static_reset() resetting the batch information. Functions
  // that are part of the Batch API and need to reset the batch information may
  // call batch_get() and manipulate the result by reference. Functions that are
  // not part of the Batch API can also do this, but shouldn't.
  static $batch = array();
  return $batch;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
