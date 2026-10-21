# LocaleJavascriptTranslationTest::testNullValuesLocalesSource()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 304–321 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L304-L321)
- **Class:** [LocaleJavascriptTranslationTest](../LocaleJavascriptTranslationTest.md)
- **Module/theme:** locale

## Signature

```php
function testNullValuesLocalesSource()
```

## Documentation

```text
Test handling of null values in JS parsing for PHP8.0+ deprecations.
```

## Code

```php
  function testNullValuesLocalesSource() {
    db_insert('locales_source')
      ->fields(array(
        'location' => NULL,
        'source' => 'Standard Call t',
        'context' => '',
        'textgroup' => 'default',
      ))
      ->execute();

    $filename = drupal_get_path('module', 'locale_test') . '/locale_test.js';

    // Parse the file to look for source strings.
    _locale_parse_js_file($filename);

    $num_records = db_select('locales_source')->fields(NULL, array('lid'))->countQuery()->execute()->fetchField();
    $this->assertEqual($num_records, 32, 'Correct number of strings parsed from JS file');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
