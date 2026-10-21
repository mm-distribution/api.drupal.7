# ProfileCrudTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 504–510 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L504-L510)
- **Class:** [ProfileCrudTestCase](../ProfileCrudTestCase.md)
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
      'name' => 'Profile CRUD tests',
      'description' => 'Test profile integration with user create, read, update, delete.',
      'group' => 'Profile',
    );
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
