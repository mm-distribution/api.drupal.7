# _drupal_error_handler()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2671–2674 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2671-L2674)

## Signature

```php
function _drupal_error_handler($error_level, $message, $filename, $line)
```

## Documentation

```text
Provides custom PHP error handling.

@param $error_level
  The level of the error raised.
@param $message
  The error message.
@param $filename
  The filename that the error was raised in.
@param $line
  The line number the error was raised at.
```

## Code

```php
function _drupal_error_handler($error_level, $message, $filename, $line) {
  require_once DRUPAL_ROOT . '/includes/errors.inc';
  _drupal_error_handler_real($error_level, $message, $filename, $line);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
