# MenuRouterTestCase::testThemeCallbackFakeTheme()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 273–277 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L273-L277)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeCallbackFakeTheme()
```

## Documentation

```text
Test the theme callback when it is set to use a theme that does not exist.
```

## Code

```php
  function testThemeCallbackFakeTheme() {
    $this->drupalGet('menu-test/theme-callback/use-fake-theme');
    $this->assertText('Custom theme: NONE. Actual theme: bartik.', 'The theme callback system falls back on the default theme when a theme that does not exist is requested.');
    $this->assertRaw('bartik/css/style.css', "The default theme's CSS appears on the page.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
