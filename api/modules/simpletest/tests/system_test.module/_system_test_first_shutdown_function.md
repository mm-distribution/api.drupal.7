# _system_test_first_shutdown_function()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 442–447 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L442-L447)
- **Module/theme:** batch_test

## Signature

```php
function _system_test_first_shutdown_function($arg1, $arg2)
```

## Documentation

```text
Dummy shutdown function which registers another shutdown function.
```

## Code

```php
function _system_test_first_shutdown_function($arg1, $arg2) {
  // Output something, page has already been printed and the session stored
  // so we can't use drupal_set_message.
  print t('First shutdown function, arg1 : @arg1, arg2: @arg2', array('@arg1' => $arg1, '@arg2' => $arg2));
  drupal_register_shutdown_function('_system_test_second_shutdown_function', $arg1, $arg2);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
