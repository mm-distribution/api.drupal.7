# ThemeHookInitTestCase::testThemeInitializationHookInit()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 423–427 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L423-L427)
- **Class:** [ThemeHookInitTestCase](../ThemeHookInitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeInitializationHookInit()
```

## Documentation

```text
Test that the theme system can generate output when called by hook_init().
```

## Code

```php
  function testThemeInitializationHookInit() {
    $this->drupalGet('theme-test/hook-init');
    $this->assertRaw('Themed output generated in hook_init()', 'Themed output generated in hook_init() correctly appears on the page.');
    $this->assertRaw('bartik/css/style.css', "The default theme's CSS appears on the page when the theme system is initialized in hook_init().");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
