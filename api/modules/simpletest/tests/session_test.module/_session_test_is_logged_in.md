# _session_test_is_logged_in()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 203–205 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L203-L205)
- **Module/theme:** batch_test

## Signature

```php
function _session_test_is_logged_in()
```

## Documentation

```text
Menu callback, only available if current user is logged in.
```

## Code

```php
function _session_test_is_logged_in() {
  return t('User is logged in.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
