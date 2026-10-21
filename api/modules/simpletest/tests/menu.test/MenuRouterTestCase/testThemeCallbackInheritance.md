# MenuRouterTestCase::testThemeCallbackInheritance()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 176–180 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L176-L180)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeCallbackInheritance()
```

## Documentation

```text
Test that the theme callback is properly inherited.
```

## Code

```php
  function testThemeCallbackInheritance() {
    $this->drupalGet('menu-test/theme-callback/use-admin-theme/inheritance');
    $this->assertText('Custom theme: seven. Actual theme: seven. Theme callback inheritance is being tested.', 'Theme callback inheritance correctly uses the administrative theme.');
    $this->assertRaw('seven/style.css', "The administrative theme's CSS appears on the page.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
