# _session_test_set_not_started()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 160–164 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L160-L164)
- **Module/theme:** batch_test

## Signature

```php
function _session_test_set_not_started()
```

## Documentation

```text
Menu callback, stores a value in $_SESSION['session_test_value'] without
having started the session in advance.
```

## Code

```php
function _session_test_set_not_started() {
  if (!drupal_session_will_start()) {
    $_SESSION['session_test_value'] = t('Session was not started');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
