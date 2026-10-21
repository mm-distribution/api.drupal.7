# LocaleUILanguageNegotiationTest::getInfo()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2352–2358 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2352-L2358)
- **Class:** [LocaleUILanguageNegotiationTest](../LocaleUILanguageNegotiationTest.md)
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
      'name' => 'UI language negotiation',
      'description' => 'Test UI language switching by URL path prefix and domain.',
      'group' => 'Locale',
    );
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
