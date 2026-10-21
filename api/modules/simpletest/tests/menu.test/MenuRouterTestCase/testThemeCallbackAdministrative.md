# MenuRouterTestCase::testThemeCallbackAdministrative()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 167–171 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L167-L171)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeCallbackAdministrative()
```

## Documentation

```text
Test the theme callback when it is set to use an administrative theme.
```

## Code

```php
  function testThemeCallbackAdministrative() {
    $this->drupalGet('menu-test/theme-callback/use-admin-theme');
    $this->assertText('Custom theme: seven. Actual theme: seven.', 'The administrative theme can be correctly set in a theme callback.');
    $this->assertRaw('seven/style.css', "The administrative theme's CSS appears on the page.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
