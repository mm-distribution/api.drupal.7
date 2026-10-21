# _system_test_second_shutdown_function()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 452–462 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L452-L462)
- **Module/theme:** batch_test

## Signature

```php
function _system_test_second_shutdown_function($arg1, $arg2)
```

## Documentation

```text
Dummy shutdown function.
```

## Code

```php
function _system_test_second_shutdown_function($arg1, $arg2) {
  // Output something, page has already been printed and the session stored
  // so we can't use drupal_set_message.
  print t('Second shutdown function, arg1 : @arg1, arg2: @arg2', array('@arg1' => $arg1, '@arg2' => $arg2));

  // Throw an exception with an HTML tag. Since this is called in a shutdown
  // function, it will not bubble up to the default exception handler but will
  // be caught in _drupal_shutdown_function() and be displayed through
  // _drupal_render_exception_safe().
  throw new Exception('Drupal is <blink>awesome</blink>.');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
