# _session_test_get()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 90–97 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L90-L97)
- **Module/theme:** batch_test

## Signature

```php
function _session_test_get()
```

## Documentation

```text
Page callback, prints the stored session value to the screen.
```

## Code

```php
function _session_test_get() {
  if (!empty($_SESSION['session_test_value'])) {
    return t('The current value of the stored session variable is: %val', array('%val' => $_SESSION['session_test_value']));
  }
  else {
    return "";
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
