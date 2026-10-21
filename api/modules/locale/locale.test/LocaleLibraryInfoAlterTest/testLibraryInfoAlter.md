# LocaleLibraryInfoAlterTest::testLibraryInfoAlter()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 205–209 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L205-L209)
- **Class:** [LocaleLibraryInfoAlterTest](../LocaleLibraryInfoAlterTest.md)
- **Module/theme:** locale

## Signature

```php
public function testLibraryInfoAlter()
```

## Documentation

```text
Verifies that the datepicker can be localized.

@see locale_library_info_alter()
```

## Code

```php
  public function testLibraryInfoAlter() {
    drupal_add_library('system', 'ui.datepicker');
    $scripts = drupal_get_js();
    $this->assertTrue(strpos($scripts, 'locale.datepicker.js'), 'locale.datepicker.js added to scripts.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
