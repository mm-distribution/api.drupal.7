# system_test_redirect()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 190–198 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L190-L198)
- **Module/theme:** batch_test

## Signature

```php
function system_test_redirect($code)
```

## Documentation

_No docblock in source._

## Code

```php
function system_test_redirect($code) {
  $code = (int) $code;
  if ($code != 200) {
    // Header names are case-insensitive.
    header("locaTION: " . url('system-test/redirect/200', array('absolute' => TRUE)), TRUE, $code);
    exit;
  }
  return '';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
