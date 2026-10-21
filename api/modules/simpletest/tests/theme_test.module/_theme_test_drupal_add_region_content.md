# _theme_test_drupal_add_region_content()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 152–155 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L152-L155)
- **Module/theme:** batch_test

## Signature

```php
function _theme_test_drupal_add_region_content()
```

## Documentation

```text
Page callback, calls drupal_add_region_content.
```

## Code

```php
function _theme_test_drupal_add_region_content() {
  drupal_add_region_content('content', 'World');
  return 'Hello';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
