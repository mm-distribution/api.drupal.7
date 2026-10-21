# openid_admin_paths()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 52–58 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L52-L58)
- **Module/theme:** openid
- **Implements:** [hook_admin_paths()](../../system/system.api.php/hook_admin_paths.md)

## Signature

```php
function openid_admin_paths()
```

## Documentation

```text
Implements hook_admin_paths().
```

## Code

```php
function openid_admin_paths() {
  $paths = array(
    'user/*/openid' => TRUE,
    'user/*/openid/delete' => TRUE,
  );
  return $paths;
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
