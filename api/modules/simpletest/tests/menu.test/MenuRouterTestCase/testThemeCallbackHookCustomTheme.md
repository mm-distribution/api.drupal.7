# MenuRouterTestCase::testThemeCallbackHookCustomTheme()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 307–318 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L307-L318)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeCallbackHookCustomTheme()
```

## Documentation

```text
Test that the theme callback wins out over hook_custom_theme().
```

## Code

```php
  function testThemeCallbackHookCustomTheme() {
    // Trigger hook_custom_theme() to dynamically request the Stark theme for
    // the requested page.
    variable_set('menu_test_hook_custom_theme_name', 'stark');
    theme_enable(array('stark'));

    // The menu "theme callback" should take precedence over a value set in
    // hook_custom_theme().
    $this->drupalGet('menu-test/theme-callback/use-admin-theme');
    $this->assertText('Custom theme: seven. Actual theme: seven.', 'The result of hook_custom_theme() does not override what was set in a theme callback.');
    $this->assertRaw('seven/style.css', "The Seven theme's CSS appears on the page.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
