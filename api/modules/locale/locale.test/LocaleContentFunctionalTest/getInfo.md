# LocaleContentFunctionalTest::getInfo()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2150–2156 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2150-L2156)
- **Class:** [LocaleContentFunctionalTest](../LocaleContentFunctionalTest.md)
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
      'name' => 'Content language settings',
      'description' => 'Checks you can enable multilingual support on content types and configure a language for a node.',
      'group' => 'Locale',
    );
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
