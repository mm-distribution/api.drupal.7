# ProfileTestFields::getInfo()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 168–174 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L168-L174)
- **Class:** [ProfileTestFields](../ProfileTestFields.md)
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
      'name' => 'Test single fields',
      'description' => 'Testing profile module with add/edit/delete textfield, textarea, list, checkbox, and url fields into profile page',
      'group' => 'Profile'
    );
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
