# MenuRouterTestCase::testThemeCallbackOptionalTheme()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 257–268 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L257-L268)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeCallbackOptionalTheme()
```

## Documentation

```text
Test the theme callback when it is set to use an optional theme.
```

## Code

```php
  function testThemeCallbackOptionalTheme() {
    // Request a theme that is not enabled.
    $this->drupalGet('menu-test/theme-callback/use-stark-theme');
    $this->assertText('Custom theme: NONE. Actual theme: bartik.', 'The theme callback system falls back on the default theme when a theme that is not enabled is requested.');
    $this->assertRaw('bartik/css/style.css', "The default theme's CSS appears on the page.");

    // Now enable the theme and request it again.
    theme_enable(array('stark'));
    $this->drupalGet('menu-test/theme-callback/use-stark-theme');
    $this->assertText('Custom theme: stark. Actual theme: stark.', 'The theme callback system uses an optional theme once it has been enabled.');
    $this->assertRaw('stark/layout.css', "The optional theme's CSS appears on the page.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
