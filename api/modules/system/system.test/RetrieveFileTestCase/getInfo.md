# RetrieveFileTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2735–2741 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2735-L2741)
- **Class:** [RetrieveFileTestCase](../RetrieveFileTestCase.md)
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
      'name' => 'HTTP file retrieval',
      'description' => 'Checks HTTP file fetching and error handling.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
