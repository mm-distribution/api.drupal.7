# _session_test_id()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 120–128 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L120-L128)
- **Module/theme:** batch_test

## Signature

```php
function _session_test_id()
```

## Documentation

```text
Menu callback: print the current session ID.
```

## Code

```php
function _session_test_id() {
  // Set a value in $_SESSION, so that drupal_session_commit() will start
  // a session.
  $_SESSION['test'] = 'test';

  drupal_session_commit();

  return 'session_id:' . session_id() . "\n";
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
