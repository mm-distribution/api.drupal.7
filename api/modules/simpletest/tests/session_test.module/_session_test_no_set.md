# _session_test_no_set()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 111–115 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L111-L115)
- **Module/theme:** batch_test

## Signature

```php
function _session_test_no_set($value)
```

## Documentation

```text
Menu callback: turns off session saving and then tries to save a value
anyway.
```

## Code

```php
function _session_test_no_set($value) {
  drupal_save_session(FALSE);
  _session_test_set($value);
  return t('session saving was disabled, and then %val was set', array('%val' => $value));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
