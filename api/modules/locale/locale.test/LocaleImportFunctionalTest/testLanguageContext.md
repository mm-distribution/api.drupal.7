# LocaleImportFunctionalTest::testLanguageContext()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1095–1103 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1095-L1103)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testLanguageContext()
```

## Documentation

```text
Test msgctxt context support.
```

## Code

```php
  function testLanguageContext() {
    // Try importing a .po file.
    $this->importPoFile($this->getPoFileWithContext(), array(
      'langcode' => 'hr',
    ));

    $this->assertIdentical(t('May', array(), array('langcode' => 'hr', 'context' => 'Long month name')), 'Svibanj', 'Long month name context is working.');
    $this->assertIdentical(t('May', array(), array('langcode' => 'hr')), 'Svi.', 'Default context is working.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
