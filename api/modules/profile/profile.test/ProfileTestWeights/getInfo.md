# ProfileTestWeights::getInfo()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 289–295 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L289-L295)
- **Class:** [ProfileTestWeights](../ProfileTestWeights.md)
- **Module/theme:** profile

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
      'name' => 'Test field weights',
      'description' => 'Testing profile modules weigting of fields',
      'group' => 'Profile'
    );
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
