# LocaleUninstallFrenchFunctionalTest

- **Type:** Class
- **File:** [`modules/locale/locale.test`](_file.md), lines 1589–1602 · [local source](../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1589-L1602)
- **Module/theme:** locale

## Signature

```php
class LocaleUninstallFrenchFunctionalTest extends LocaleUninstallFunctionalTest
```

## Documentation

```text
Locale uninstall with French UI functional test.

Because this class extends LocaleUninstallFunctionalTest, it doesn't require a new
test of its own. Rather, it switches the default UI language in setUp and then
runs the testUninstallProcess (which it inherits from LocaleUninstallFunctionalTest)
to test with this new language.
```

## Methods (derived index)

- [getInfo()](LocaleUninstallFrenchFunctionalTest/getInfo.md)
- [setUp()](LocaleUninstallFrenchFunctionalTest/setUp.md)

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
