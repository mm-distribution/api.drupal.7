# forum_permission()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 464–471 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L464-L471)
- **Module/theme:** forum
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function forum_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function forum_permission() {
  $perms = array(
    'administer forums' => array(
      'title' => t('Administer forums'),
    ),
  );
  return $perms;
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
