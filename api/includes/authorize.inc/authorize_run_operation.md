# authorize_run_operation()

- **Type:** Function
- **File:** [`includes/authorize.inc`](_file.md), lines 290–300 · [local source](../../../source/includes/authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc#L290-L300)

## Signature

```php
function authorize_run_operation($filetransfer)
```

## Documentation

```text
Runs the operation specified in $_SESSION['authorize_operation'].

@param $filetransfer
  The FileTransfer object to use for running the operation.
```

## Code

```php
function authorize_run_operation($filetransfer) {
  $operation = $_SESSION['authorize_operation'];
  unset($_SESSION['authorize_operation']);

  if (!empty($operation['page_title'])) {
    drupal_set_title($operation['page_title']);
  }

  require_once DRUPAL_ROOT . '/' . $operation['file'];
  call_user_func_array($operation['callback'], array_merge(array($filetransfer), $operation['arguments']));
}
```

---
_Drupal 7.103 · [includes/authorize.inc](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
