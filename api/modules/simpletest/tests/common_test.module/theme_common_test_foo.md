# theme_common_test_foo()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 236–238 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L236-L238)
- **Module/theme:** batch_test

## Signature

```php
function theme_common_test_foo($variables)
```

## Documentation

```text
Theme function for testing drupal_render() theming.
```

## Code

```php
function theme_common_test_foo($variables) {
  return $variables['foo'] . $variables['bar'];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
