# ThemeTestCase::testThemeGetSetting()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 152–157 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L152-L157)
- **Class:** [ThemeTestCase](../ThemeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeGetSetting()
```

## Documentation

```text
Test the theme_get_setting() function.
```

## Code

```php
  function testThemeGetSetting() {
    $GLOBALS['theme_key'] = 'test_theme';
    $this->assertIdentical(theme_get_setting('theme_test_setting'), 'default value', 'theme_get_setting() uses the default theme automatically.');
    $this->assertNotEqual(theme_get_setting('subtheme_override', 'test_basetheme'), theme_get_setting('subtheme_override', 'test_subtheme'), 'Base theme\'s default settings values can be overridden by subtheme.');
    $this->assertIdentical(theme_get_setting('basetheme_only', 'test_subtheme'), 'base theme value', 'Base theme\'s default settings values are inherited by subtheme.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
