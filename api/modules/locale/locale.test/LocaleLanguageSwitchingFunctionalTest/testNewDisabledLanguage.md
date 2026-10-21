# LocaleLanguageSwitchingFunctionalTest::testNewDisabledLanguage()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1684–1687 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1684-L1687)
- **Class:** [LocaleLanguageSwitchingFunctionalTest](../LocaleLanguageSwitchingFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testNewDisabledLanguage()
```

## Documentation

```text
Tests that languages can be added as disabled.
```

## Code

```php
  function testNewDisabledLanguage() {
    // Add new language which will be disabled.
    locale_add_language('de', 'German', 'Deutsch', LANGUAGE_LTR, '', '', FALSE, FALSE);
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
