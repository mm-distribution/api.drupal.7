# node_admin_paths()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 258–271 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L258-L271)
- **Module/theme:** node
- **Implements:** [hook_admin_paths()](../../system/system.api.php/hook_admin_paths.md)

## Signature

```php
function node_admin_paths()
```

## Documentation

```text
Implements hook_admin_paths().
```

## Code

```php
function node_admin_paths() {
  if (variable_get('node_admin_theme')) {
    $paths = array(
      'node/*/edit' => TRUE,
      'node/*/delete' => TRUE,
      'node/*/revisions' => TRUE,
      'node/*/revisions/*/revert' => TRUE,
      'node/*/revisions/*/delete' => TRUE,
      'node/add' => TRUE,
      'node/add/*' => TRUE,
    );
    return $paths;
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
