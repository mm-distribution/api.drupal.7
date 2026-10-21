# test_theme_theme_test__suggestion()

- **Type:** Function
- **File:** [`modules/simpletest/tests/themes/test_theme/template.php`](_file.md), lines 6–8 · [local source](../../../../../../../source/modules/simpletest/tests/themes/test_theme/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/test_theme/template.php#L6-L8)
- **Module/theme:** test_theme

## Signature

```php
function test_theme_theme_test__suggestion($variables)
```

## Documentation

```text
Tests a theme overriding a suggestion of a base theme hook.
```

## Code

```php
function test_theme_theme_test__suggestion($variables) {
  return 'Theme hook implementor=test_theme_theme_test__suggestion(). Foo=' . $variables['foo'];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/themes/test_theme/template.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/test_theme/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
