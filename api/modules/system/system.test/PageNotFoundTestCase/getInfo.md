# PageNotFoundTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1139–1145 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1139-L1145)
- **Class:** [PageNotFoundTestCase](../PageNotFoundTestCase.md)
- **Module/theme:** system

## Signature

```php
public static function getInfo()
```

## Documentation

```text
Implement getInfo().
```

## Code

```php
  public static function getInfo() {
    return array(
      'name' => '404 functionality',
      'description' => "Tests page not found functionality, including custom 404 pages.",
      'group' => 'System'
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
