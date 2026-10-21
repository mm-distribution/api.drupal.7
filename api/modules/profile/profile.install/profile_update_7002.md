# profile_update_7002()

- **Type:** Function
- **File:** [`modules/profile/profile.install`](_file.md), lines 165–172 · [local source](../../../../source/modules/profile/profile.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.install#L165-L172)
- **Module/theme:** profile

## Signature

```php
function profile_update_7002()
```

## Documentation

```text
Change the weight column to normal int.
```

## Code

```php
function profile_update_7002() {
  db_change_field('profile_field', 'weight', 'weight', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'Weight of field in relation to other profile fields.',
  ));
}
```

---
_Drupal 7.103 · [modules/profile/profile.install](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.install) · Licensed GPL-2.0-or-later (see LICENSE)._
