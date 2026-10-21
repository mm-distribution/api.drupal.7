# system_test_drupal_set_message()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 510–519 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L510-L519)
- **Module/theme:** batch_test

## Signature

```php
function system_test_drupal_set_message()
```

## Documentation

```text
Sets two messages and removes the first one before the messages are displayed.
```

## Code

```php
function system_test_drupal_set_message() {
  // Set two messages.
  drupal_set_message('First message (removed).');
  drupal_set_message('Second message (not removed).');

  // Remove the first.
  unset($_SESSION['messages']['status'][0]);

  return '';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
