# _session_test_id_from_cookie()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 133–135 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L133-L135)
- **Module/theme:** batch_test

## Signature

```php
function _session_test_id_from_cookie()
```

## Documentation

```text
Menu callback: print the current session ID as read from the cookie.
```

## Code

```php
function _session_test_id_from_cookie() {
  return 'session_id:' . $_COOKIE[session_name()] . "\n";
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
