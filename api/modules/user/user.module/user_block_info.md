# user_block_info()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1385–1401 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1385-L1401)
- **Module/theme:** user
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function user_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function user_block_info() {
  global $user;

  $blocks['login']['info'] = t('User login');
  // Not worth caching.
  $blocks['login']['cache'] = DRUPAL_NO_CACHE;

  $blocks['new']['info'] = t('Who\'s new');
  $blocks['new']['properties']['administrative'] = TRUE;

  // Too dynamic to cache.
  $blocks['online']['info'] = t('Who\'s online');
  $blocks['online']['cache'] = DRUPAL_NO_CACHE;
  $blocks['online']['properties']['administrative'] = TRUE;

  return $blocks;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
