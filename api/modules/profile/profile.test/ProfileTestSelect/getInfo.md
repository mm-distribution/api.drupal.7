# ProfileTestSelect::getInfo()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 212–218 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L212-L218)
- **Class:** [ProfileTestSelect](../ProfileTestSelect.md)
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
      'name' => 'Test select field',
      'description' => 'Testing profile module with add/edit/delete a select field',
      'group' => 'Profile'
    );
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
