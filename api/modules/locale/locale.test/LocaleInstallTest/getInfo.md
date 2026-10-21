# LocaleInstallTest::getInfo()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1434–1440 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1434-L1440)
- **Class:** [LocaleInstallTest](../LocaleInstallTest.md)
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
      'name' => 'String translation using st()',
      'description' => 'Tests that st() works like t().',
      'group' => 'Locale',
    );
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
