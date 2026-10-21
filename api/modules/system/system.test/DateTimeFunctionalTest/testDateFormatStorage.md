# DateTimeFunctionalTest::testDateFormatStorage()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1462–1525 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1462-L1525)
- **Class:** [DateTimeFunctionalTest](../DateTimeFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testDateFormatStorage()
```

## Documentation

```text
Test if the date formats are stored properly.
```

## Code

```php
  function testDateFormatStorage() {
    $date_format = array(
      'type' => 'short',
      'format' => 'dmYHis',
      'locked' => 0,
      'is_new' => 1,
    );
    system_date_format_save($date_format);

    $format = db_select('date_formats', 'df')
      ->fields('df', array('format'))
      ->condition('type', 'short')
      ->condition('format', 'dmYHis')
      ->execute()
      ->fetchField();
    $this->verbose($format);
    $this->assertEqual('dmYHis', $format, 'Unlocalized date format resides in general table.');

    $format = db_select('date_format_locale', 'dfl')
      ->fields('dfl', array('format'))
      ->condition('type', 'short')
      ->condition('format', 'dmYHis')
      ->execute()
      ->fetchField();
    $this->assertFalse($format, 'Unlocalized date format resides not in localized table.');

    // Enable German language
    locale_add_language('de', NULL, NULL, LANGUAGE_LTR, '', '', TRUE, 'en');

    $date_format = array(
      'type' => 'short',
      'format' => 'YMDHis',
      'locales' => array('de', 'tr'),
      'locked' => 0,
      'is_new' => 1,
    );
    system_date_format_save($date_format);

    $format = db_select('date_format_locale', 'dfl')
      ->fields('dfl', array('format'))
      ->condition('type', 'short')
      ->condition('format', 'YMDHis')
      ->condition('language', 'de')
      ->execute()
      ->fetchField();
    $this->assertEqual('YMDHis', $format, 'Localized date format resides in localized table.');

    $format = db_select('date_formats', 'df')
      ->fields('df', array('format'))
      ->condition('type', 'short')
      ->condition('format', 'YMDHis')
      ->execute()
      ->fetchField();
    $this->assertEqual('YMDHis', $format, 'Localized date format resides in general table too.');

    $format = db_select('date_format_locale', 'dfl')
      ->fields('dfl', array('format'))
      ->condition('type', 'short')
      ->condition('format', 'YMDHis')
      ->condition('language', 'tr')
      ->execute()
      ->fetchColumn();
    $this->assertFalse($format, 'Localized date format for disabled language is ignored.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
