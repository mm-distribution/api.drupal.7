# _session_test_set_message_but_dont_save()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 151–154 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L151-L154)
- **Module/theme:** batch_test

## Signature

```php
function _session_test_set_message_but_dont_save()
```

## Documentation

```text
Menu callback, sets a message but call drupal_save_session(FALSE).
```

## Code

```php
function _session_test_set_message_but_dont_save() {
  drupal_save_session(FALSE);
  _session_test_set_message();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
