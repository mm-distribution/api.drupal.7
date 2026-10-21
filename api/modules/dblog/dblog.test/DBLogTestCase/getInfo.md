# DBLogTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 27–33 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L27-L33)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

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
      'name' => 'DBLog functionality',
      'description' => 'Generate events and verify dblog entries; verify user access to log reports based on persmissions.',
      'group' => 'DBLog',
    );
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
