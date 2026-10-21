# theme_theme_test_foo()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 169–171 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L169-L171)
- **Module/theme:** batch_test

## Signature

```php
function theme_theme_test_foo($variables)
```

## Documentation

```text
Theme function for testing theme('theme_test_foo').
```

## Code

```php
function theme_theme_test_foo($variables) {
  return $variables['foo'];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
