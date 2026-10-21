# user_file_download_access()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 4143–4147 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L4143-L4147)
- **Module/theme:** user
- **Implements:** [hook_file_download_access()](../../file/file.api.php/hook_file_download_access.md)

## Signature

```php
function user_file_download_access($field, $entity_type, $entity)
```

## Documentation

```text
Implements hook_file_download_access().
```

## Code

```php
function user_file_download_access($field, $entity_type, $entity) {
  if ($entity_type == 'user') {
    return user_view_access($entity);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
