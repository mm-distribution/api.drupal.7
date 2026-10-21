# _update_batch_create_message()

- **Type:** Function
- **File:** [`modules/update/update.authorize.inc`](_file.md), lines 313–315 · [local source](../../../../source/modules/update/update.authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc#L313-L315)
- **Module/theme:** update

## Signature

```php
function _update_batch_create_message(&$project_results, $message, $success = TRUE)
```

## Documentation

```text
Creates a structure of log messages.

@param array $project_results
  An associative array of results from the batch operation.
@param string $message
  A string containing a log message.
@param bool $success
  (optional) TRUE if the operation the message is about was a success, FALSE
  if there were errors. Defaults to TRUE.
```

## Code

```php
function _update_batch_create_message(&$project_results, $message, $success = TRUE) {
  $project_results[] = array('message' => $message, 'success' => $success);
}
```

---
_Drupal 7.103 · [modules/update/update.authorize.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
