# InfoFileParserTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2367–2373 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2367-L2373)
- **Class:** [InfoFileParserTestCase](../InfoFileParserTestCase.md)
- **Module/theme:** system

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
      'name' => 'Info file format parser',
      'description' => 'Tests proper parsing of a .info file formatted string.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
