# _session_test_set()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 102–105 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L102-L105)
- **Module/theme:** batch_test

## Signature

```php
function _session_test_set($value)
```

## Documentation

```text
Page callback, stores a value in $_SESSION['session_test_value'].
```

## Code

```php
function _session_test_set($value) {
  $_SESSION['session_test_value'] = $value;
  return t('The current value of the stored session variable has been set to %val', array('%val' => $value));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
