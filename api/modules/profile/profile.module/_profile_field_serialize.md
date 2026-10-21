# _profile_field_serialize()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 610–612 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L610-L612)
- **Module/theme:** profile

## Signature

```php
function _profile_field_serialize($type = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
function _profile_field_serialize($type = NULL) {
  return $type == 'date';
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
