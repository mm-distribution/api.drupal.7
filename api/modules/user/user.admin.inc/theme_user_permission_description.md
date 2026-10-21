# theme_user_permission_description()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 839–853 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L839-L853)
- **Module/theme:** user
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_user_permission_description($variables)
```

## Documentation

```text
Returns HTML for an individual permission description.

@param $variables
  An associative array containing:
  - permission_item: An associative array representing the permission whose
    description is being themed. Useful keys include:
    - description: The text of the permission description.
    - warning: A security-related warning message about the permission (if
      there is one).
  - hide: A boolean indicating whether or not the permission description was
    requested to be hidden rather than shown.

@ingroup themeable
```

## Code

```php
function theme_user_permission_description($variables) {
  if (!$variables['hide']) {
    $description = array();
    $permission_item = $variables['permission_item'];
    if (!empty($permission_item['description'])) {
      $description[] = $permission_item['description'];
    }
    if (!empty($permission_item['warning'])) {
      $description[] = '<em class="permission-warning">' . $permission_item['warning'] . '</em>';
    }
    if (!empty($description)) {
      return implode(' ', $description);
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
