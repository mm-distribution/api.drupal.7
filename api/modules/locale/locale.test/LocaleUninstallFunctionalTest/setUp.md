# LocaleUninstallFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1476–1479 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1476-L1479)
- **Class:** [LocaleUninstallFunctionalTest](../LocaleUninstallFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('locale');
    $this->language = 'en';
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
