# _theme_test_suggestion()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 145–147 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L145-L147)
- **Module/theme:** batch_test

## Signature

```php
function _theme_test_suggestion()
```

## Documentation

```text
Page callback, calls a theme hook suggestion.
```

## Code

```php
function _theme_test_suggestion() {
  return theme(array('theme_test__suggestion', 'theme_test'), array());
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
