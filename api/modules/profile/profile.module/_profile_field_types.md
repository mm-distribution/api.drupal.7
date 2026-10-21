# _profile_field_types()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 599–608 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L599-L608)
- **Module/theme:** profile

## Signature

```php
function _profile_field_types($type = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
function _profile_field_types($type = NULL) {
  $types = array('textfield' => t('single-line textfield'),
                 'textarea' => t('multi-line textfield'),
                 'checkbox' => t('checkbox'),
                 'selection' => t('list selection'),
                 'list' => t('freeform list'),
                 'url' => t('URL'),
                 'date' => t('date'));
  return isset($type) ? $types[$type] : $types;
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
