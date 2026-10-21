# LocaleImportFunctionalTest::testEmptyMsgstr()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1108–1140 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1108-L1140)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testEmptyMsgstr()
```

## Documentation

```text
Test empty msgstr at end of .po file see #611786.
```

## Code

```php
  function testEmptyMsgstr() {
    $langcode = 'hu';

    // Try importing a .po file.
    $this->importPoFile($this->getPoFileWithMsgstr(), array(
      'langcode' => $langcode,
    ));

    $this->assertRaw(t('The translation was successfully imported. There are %number newly created translated strings, %update strings were updated and %delete strings were removed.', array('%number' => 1, '%update' => 0, '%delete' => 0)), 'The translation file was successfully imported.');
    $this->assertIdentical(t('Operations', array(), array('langcode' => $langcode)), 'Műveletek', 'String imported and translated.');

    // Try importing a .po file.
    $this->importPoFile($this->getPoFileWithEmptyMsgstr(), array(
      'langcode' => $langcode,
      'mode' => 0,
    ));
    $this->assertRaw(t('The translation was successfully imported. There are %number newly created translated strings, %update strings were updated and %delete strings were removed.', array('%number' => 0, '%update' => 0, '%delete' => 1)), 'The translation file was successfully imported.');
    // This is the language indicator on the translation search screen for
    // untranslated strings. Copied straight from locale.inc.
    $language_indicator = "<em class=\"locale-untranslated\">$langcode</em> ";
    $str = "Operations";
    $search = array(
      'string' => $str,
      'language' => 'all',
      'translation' => 'all',
      'group' => 'all',
    );
    $this->drupalPost('admin/config/regional/translate/translate', $search, t('Filter'));
    // assertText() seems to remove the input field where $str always could be
    // found, so this is not a false assert.
    $this->assertText($str, 'Search found the string.');
    $this->assertRaw($language_indicator, 'String is untranslated again.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
