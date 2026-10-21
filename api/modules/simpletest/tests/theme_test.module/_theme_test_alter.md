# _theme_test_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 136–140 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L136-L140)
- **Module/theme:** batch_test

## Signature

```php
function _theme_test_alter()
```

## Documentation

```text
Page callback, calls drupal_alter().

This is for testing that the theme can have hook_*_alter() implementations
that run during page callback execution, even before theme() is called for
the first time.
```

## Code

```php
function _theme_test_alter() {
  $data = 'foo';
  drupal_alter('theme_test_alter', $data);
  return "The altered data is $data.";
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
