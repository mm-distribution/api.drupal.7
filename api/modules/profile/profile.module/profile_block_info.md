# profile_block_info()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 139–143 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L139-L143)
- **Module/theme:** profile
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function profile_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
 function profile_block_info() {
  $blocks['author-information']['info'] = t('Author information');
  $blocks['author-information']['cache'] = DRUPAL_CACHE_PER_PAGE | DRUPAL_CACHE_PER_ROLE;
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
