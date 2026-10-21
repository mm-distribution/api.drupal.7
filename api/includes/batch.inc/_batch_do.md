# _batch_do()

- **Type:** Function
- **File:** [`includes/batch.inc`](_file.md), lines 103–109 · [local source](../../../source/includes/batch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc#L103-L109)

## Signature

```php
function _batch_do()
```

## Documentation

```text
Does one execution pass with JavaScript and returns progress to the browser.

@see _batch_process()
```

## Code

```php
function _batch_do() {

  // Perform actual processing.
  list($percentage, $message) = _batch_process();

  drupal_json_output(array('status' => TRUE, 'percentage' => $percentage, 'message' => $message));
}
```

---
_Drupal 7.103 · [includes/batch.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
