# user_filters()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3497–3540 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3497-L3540)
- **Module/theme:** user

## Signature

```php
function user_filters()
```

## Documentation

```text
List user administration filters that can be applied.
```

## Code

```php
function user_filters() {
  // Regular filters
  $filters = array();
  $roles = user_roles(TRUE);
  unset($roles[DRUPAL_AUTHENTICATED_RID]); // Don't list authorized role.
  if (count($roles)) {
    $filters['role'] = array(
      'title' => t('role'),
      'field' => 'ur.rid',
      'options' => array(
        '[any]' => t('any'),
      ) + $roles,
    );
  }

  $options = array();
  foreach (module_implements('permission') as $module) {
    $function = $module . '_permission';
    if ($permissions = $function()) {
      asort($permissions);
      foreach ($permissions as $permission => $description) {
        $options[t('@module module', array('@module' => $module))][$permission] = t($permission);
      }
    }
  }
  ksort($options);
  $filters['permission'] = array(
    'title' => t('permission'),
    'options' => array(
      '[any]' => t('any'),
    ) + $options,
  );

  $filters['status'] = array(
    'title' => t('status'),
    'field' => 'u.status',
    'options' => array(
      '[any]' => t('any'),
      1 => t('active'),
      0 => t('blocked'),
    ),
  );
  return $filters;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
