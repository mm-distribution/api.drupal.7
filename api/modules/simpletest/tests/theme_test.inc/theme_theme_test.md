# theme_theme_test()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.inc`](_file.md), lines 6–8 · [local source](../../../../../source/modules/simpletest/tests/theme_test.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.inc#L6-L8)
- **Module/theme:** batch_test

## Signature

```php
function theme_theme_test($variables)
```

## Documentation

```text
Returns HTML for the 'theme_test' theme hook used by tests.
```

## Code

```php
function theme_theme_test($variables) {
  return 'Theme hook implementor=theme_theme_test(). Foo=' . $variables['foo'];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
