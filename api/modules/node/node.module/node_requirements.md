# node_requirements()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 4116–4138 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L4116-L4138)
- **Module/theme:** node
- **Implements:** [hook_requirements()](../../system/system.api.php/hook_requirements.md)

## Signature

```php
function node_requirements($phase)
```

## Documentation

```text
Implements hook_requirements().
```

## Code

```php
function node_requirements($phase) {
  $requirements = array();
  if ($phase === 'runtime') {
    // Only show rebuild button if there are either 0, or 2 or more, rows
    // in the {node_access} table, or if there are modules that
    // implement hook_node_grants().
    $grant_count = db_query('SELECT COUNT(*) FROM {node_access}')->fetchField();
    if ($grant_count != 1 || count(module_implements('node_grants')) > 0) {
      $value = format_plural($grant_count, 'One permission in use', '@count permissions in use', array('@count' => $grant_count));
    }
    else {
      $value = t('Disabled');
    }
    $description = t('If the site is experiencing problems with permissions to content, you may have to rebuild the permissions cache. Rebuilding will remove all privileges to content and replace them with permissions based on the current modules and settings. Rebuilding may take some time if there is a lot of content or complex permission settings. After rebuilding has completed, content will automatically use the new permissions.');

    $requirements['node_access'] = array(
      'title' => t('Node Access Permissions'),
      'value' => $value,
      'description' => $description . ' ' . l(t('Rebuild permissions'), 'admin/reports/status/rebuild'),
    );
  }
  return $requirements;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
