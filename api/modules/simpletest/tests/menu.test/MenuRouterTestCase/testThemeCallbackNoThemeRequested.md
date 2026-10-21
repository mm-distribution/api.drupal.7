# MenuRouterTestCase::testThemeCallbackNoThemeRequested()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 282–286 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L282-L286)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeCallbackNoThemeRequested()
```

## Documentation

```text
Test the theme callback when no theme is requested.
```

## Code

```php
  function testThemeCallbackNoThemeRequested() {
    $this->drupalGet('menu-test/theme-callback/no-theme-requested');
    $this->assertText('Custom theme: NONE. Actual theme: bartik.', 'The theme callback system falls back on the default theme when no theme is requested.');
    $this->assertRaw('bartik/css/style.css', "The default theme's CSS appears on the page.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
