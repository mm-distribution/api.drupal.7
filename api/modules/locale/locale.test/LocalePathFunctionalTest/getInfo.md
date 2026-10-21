# LocalePathFunctionalTest::getInfo()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2011–2017 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2011-L2017)
- **Class:** [LocalePathFunctionalTest](../LocalePathFunctionalTest.md)
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
      'name' => 'Path language settings',
      'description' => 'Checks you can configure a language for individual URL aliases.',
      'group' => 'Locale',
    );
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
