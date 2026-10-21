# IPAddressBlockingTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 702–708 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L702-L708)
- **Class:** [IPAddressBlockingTestCase](../IPAddressBlockingTestCase.md)
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
      'name' => 'IP address blocking',
      'description' => 'Test IP address blocking.',
      'group' => 'System'
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
