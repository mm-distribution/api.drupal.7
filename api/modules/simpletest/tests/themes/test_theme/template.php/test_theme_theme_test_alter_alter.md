# test_theme_theme_test_alter_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/themes/test_theme/template.php`](_file.md), lines 17–19 · [local source](../../../../../../../source/modules/simpletest/tests/themes/test_theme/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/test_theme/template.php#L17-L19)
- **Module/theme:** test_theme

## Signature

```php
function test_theme_theme_test_alter_alter(&$data)
```

## Documentation

```text
Tests a theme implementing an alter hook.

The confusing function name here is due to this being an implementation of
the alter hook invoked when the 'theme_test' module calls
drupal_alter('theme_test_alter').
```

## Code

```php
function test_theme_theme_test_alter_alter(&$data) {
  $data = 'test_theme_theme_test_alter_alter was invoked';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/themes/test_theme/template.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/test_theme/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
