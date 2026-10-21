# _session_test_set_message()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 140–146 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L140-L146)
- **Module/theme:** batch_test

## Signature

```php
function _session_test_set_message()
```

## Documentation

```text
Menu callback, sets a message to me displayed on the following page.
```

## Code

```php
function _session_test_set_message() {
  drupal_set_message(t('This is a dummy message.'));
  print t('A message was set.');
  // Do not return anything, so the current request does not result in a themed
  // page with messages. The message will be displayed in the following request
  // instead.
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
