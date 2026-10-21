# template_preprocess_theme_test()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.inc`](_file.md), lines 13–15 · [local source](../../../../../source/modules/simpletest/tests/theme_test.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.inc#L13-L15)
- **Module/theme:** batch_test

## Signature

```php
function template_preprocess_theme_test(&$variables)
```

## Documentation

```text
Preprocesses variables for theme_theme_test().
```

## Code

```php
function template_preprocess_theme_test(&$variables) {
  $variables['foo'] = 'template_preprocess_theme_test';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
