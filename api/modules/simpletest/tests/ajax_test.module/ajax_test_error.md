# ajax_test_error()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_test.module`](_file.md), lines 57–63 · [local source](../../../../../source/modules/simpletest/tests/ajax_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_test.module#L57-L63)
- **Module/theme:** batch_test

## Signature

```php
function ajax_test_error()
```

## Documentation

```text
Menu callback; Returns Ajax element with #error property set.
```

## Code

```php
function ajax_test_error() {
  $message = '';
  if (!empty($_GET['message'])) {
    $message = $_GET['message'];
  }
  return array('#type' => 'ajax', '#error' => $message);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
