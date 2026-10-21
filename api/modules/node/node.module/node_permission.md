# node_permission()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1567–1609 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1567-L1609)
- **Module/theme:** node
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function node_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function node_permission() {
  $perms = array(
    'bypass node access' => array(
      'title' => t('Bypass content access control'),
      'description' => t('View, edit and delete all content regardless of permission restrictions.'),
      'restrict access' => TRUE,
    ),
    'administer content types' => array(
      'title' => t('Administer content types'),
      'restrict access' => TRUE,
    ),
    'administer nodes' => array(
      'title' => t('Administer content'),
      'restrict access' => TRUE,
    ),
    'access content overview' => array(
      'title' => t('Access the content overview page'),
      'description' => t('Get an overview of <a href="@url">all content</a>.', array('@url' => url('admin/content'))),
    ),
    'access content' => array(
      'title' => t('View published content'),
    ),
    'view own unpublished content' => array(
      'title' => t('View own unpublished content'),
    ),
    'view revisions' => array(
      'title' => t('View content revisions'),
    ),
    'revert revisions' => array(
      'title' => t('Revert content revisions'),
    ),
    'delete revisions' => array(
      'title' => t('Delete content revisions'),
    ),
  );

  // Generate standard node permissions for all applicable node types.
  foreach (node_permissions_get_configured_types() as $type) {
    $perms += node_list_permissions($type);
  }

  return $perms;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
