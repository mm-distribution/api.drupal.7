# ModuleProvidedThemeEngineTestCase::testEngineIsFoundAndWorking()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 694–700 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L694-L700)
- **Class:** [ModuleProvidedThemeEngineTestCase](../ModuleProvidedThemeEngineTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEngineIsFoundAndWorking()
```

## Documentation

```text
Ensures that the module provided theme engine is found and used by core.
```

## Code

```php
  function testEngineIsFoundAndWorking() {
    variable_set('theme_default', 'test_theme_nyan_cat');
    variable_set('admin_theme', 'test_theme_nyan_cat');

    $this->drupalGet('theme-test/engine-info-test');
    $this->assertText('Miaou');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
