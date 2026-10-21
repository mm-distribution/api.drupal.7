# MenuRouterTestCase::testHookCustomTheme()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 291–302 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L291-L302)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHookCustomTheme()
```

## Documentation

```text
Test that hook_custom_theme() can control the theme of a page.
```

## Code

```php
  function testHookCustomTheme() {
    // Trigger hook_custom_theme() to dynamically request the Stark theme for
    // the requested page.
    variable_set('menu_test_hook_custom_theme_name', 'stark');
    theme_enable(array('stark'));

    // Visit a page that does not implement a theme callback. The above request
    // should be honored.
    $this->drupalGet('menu-test/no-theme-callback');
    $this->assertText('Custom theme: stark. Actual theme: stark.', 'The result of hook_custom_theme() is used as the theme for the current page.');
    $this->assertRaw('stark/layout.css', "The Stark theme's CSS appears on the page.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
