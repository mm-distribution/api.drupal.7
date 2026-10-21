# AdminMetaTagTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1027–1033 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1027-L1033)
- **Class:** [AdminMetaTagTestCase](../AdminMetaTagTestCase.md)
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
      'name' => 'Fingerprinting meta tag',
      'description' => 'Confirm that the fingerprinting meta tag appears as expected.',
      'group' => 'System'
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
