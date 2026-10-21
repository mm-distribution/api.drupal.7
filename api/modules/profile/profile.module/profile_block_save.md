# profile_block_save()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 169–171 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L169-L171)
- **Module/theme:** profile
- **Implements:** [hook_block_save()](../../block/block.api.php/hook_block_save.md)

## Signature

```php
function profile_block_save($delta = '', $edit = array())
```

## Documentation

```text
Implements hook_block_save().
```

## Code

```php
function profile_block_save($delta = '', $edit = array()) {
  variable_set('profile_block_author_fields', $edit['profile_block_author_fields']);
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
