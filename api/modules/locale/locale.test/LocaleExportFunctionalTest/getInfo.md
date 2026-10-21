# LocaleExportFunctionalTest::getInfo()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1352–1358 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1352-L1358)
- **Class:** [LocaleExportFunctionalTest](../LocaleExportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Translation export',
      'description' => 'Tests the exportation of locale files.',
      'group' => 'Locale',
    );
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
