# ModuleProvidedThemeEngineTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 686–689 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L686-L689)
- **Class:** [ModuleProvidedThemeEngineTestCase](../ModuleProvidedThemeEngineTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('theme_test');
    theme_enable(array('test_theme', 'test_theme_nyan_cat'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
