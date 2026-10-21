# node_menu()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1976–2155 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1976-L2155)
- **Module/theme:** node
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function node_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function node_menu() {
  $items['admin/content'] = array(
    'title' => 'Content',
    'description' => 'Find and manage content.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('node_admin_content'),
    'access arguments' => array('access content overview'),
    'weight' => -10,
    'file' => 'node.admin.inc',
  );
  $items['admin/content/node'] = array(
    'title' => 'Content',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );

  $items['admin/reports/status/rebuild'] = array(
    'title' => 'Rebuild permissions',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('node_configure_rebuild_confirm'),
    // Any user than can potentially trigger a node_access_needs_rebuild(TRUE)
    // has to be allowed access to the 'node access rebuild' confirm form.
    'access arguments' => array('access administration pages'),
    'type' => MENU_CALLBACK,
    'file' => 'node.admin.inc',
  );

  $items['admin/structure/types'] = array(
    'title' => 'Content types',
    'description' => 'Manage content types, including default status, front page promotion, comment settings, etc.',
    'page callback' => 'node_overview_types',
    'access arguments' => array('administer content types'),
    'file' => 'content_types.inc',
  );
  $items['admin/structure/types/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['admin/structure/types/add'] = array(
    'title' => 'Add content type',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('node_type_form'),
    'access arguments' => array('administer content types'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'content_types.inc',
  );
  $items['admin/structure/types/manage/%node_type'] = array(
    'title' => 'Edit content type',
    'title callback' => 'node_type_page_title',
    'title arguments' => array(4),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('node_type_form', 4),
    'access arguments' => array('administer content types'),
    'file' => 'content_types.inc',
  );
  $items['admin/structure/types/manage/%node_type/edit'] = array(
    'title' => 'Edit',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['admin/structure/types/manage/%node_type/delete'] = array(
    'title' => 'Delete',
    'page arguments' => array('node_type_delete_confirm', 4),
    'access arguments' => array('administer content types'),
    'file' => 'content_types.inc',
  );

  $items['node'] = array(
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
    'menu_name' => 'navigation',
    'type' => MENU_CALLBACK,
  );
  $items['node/add'] = array(
    'title' => 'Add content',
    'page callback' => 'node_add_page',
    'access callback' => '_node_add_access',
    'file' => 'node.pages.inc',
  );
  $items['rss.xml'] = array(
    'title' => 'RSS feed',
    'page callback' => 'node_feed',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
    // Pass a FALSE and array argument to ensure that additional path components
    // are not passed to node_feed().
    'page arguments' => array(FALSE, array()),
  );
  // @todo Remove this loop when we have a 'description callback' property.
  // Reset internal static cache of _node_types_build(), forces to rebuild the
  // node type information.
  node_type_cache_reset();
  foreach (node_type_get_types() as $type) {
    $type_url_str = str_replace('_', '-', $type->type);
    $items['node/add/' . $type_url_str] = array(
      'title' => $type->name,
      'title callback' => 'check_plain',
      'page callback' => 'node_add',
      'page arguments' => array($type->type),
      'access callback' => 'node_access',
      'access arguments' => array('create', $type->type),
      'description' => $type->description,
      'file' => 'node.pages.inc',
    );
  }
  $items['node/%node'] = array(
    'title callback' => 'node_page_title',
    'title arguments' => array(1),
    // The page callback also invokes drupal_set_title() in case
    // the menu router's title is overridden by a menu link.
    'page callback' => 'node_page_view',
    'page arguments' => array(1),
    'access callback' => 'node_access',
    'access arguments' => array('view', 1),
  );
  $items['node/%node/view'] = array(
    'title' => 'View',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['node/%node/edit'] = array(
    'title' => 'Edit',
    'page callback' => 'node_page_edit',
    'page arguments' => array(1),
    'access callback' => 'node_access',
    'access arguments' => array('update', 1),
    'weight' => 0,
    'type' => MENU_LOCAL_TASK,
    'context' => MENU_CONTEXT_PAGE | MENU_CONTEXT_INLINE,
    'file' => 'node.pages.inc',
  );
  $items['node/%node/delete'] = array(
    'title' => 'Delete',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('node_delete_confirm', 1),
    'access callback' => 'node_access',
    'access arguments' => array('delete', 1),
    'weight' => 1,
    'type' => MENU_LOCAL_TASK,
    'context' => MENU_CONTEXT_INLINE,
    'file' => 'node.pages.inc',
  );
  $items['node/%node/revisions'] = array(
    'title' => 'Revisions',
    'page callback' => 'node_revision_overview',
    'page arguments' => array(1),
    'access callback' => '_node_revision_access',
    'access arguments' => array(1),
    'weight' => 2,
    'type' => MENU_LOCAL_TASK,
    'file' => 'node.pages.inc',
  );
  $items['node/%node/revisions/%/view'] = array(
    'title' => 'Revisions',
    'load arguments' => array(3),
    'page callback' => 'node_show',
    'page arguments' => array(1, TRUE),
    'access callback' => '_node_revision_access',
    'access arguments' => array(1),
  );
  $items['node/%node/revisions/%/revert'] = array(
    'title' => 'Revert to earlier revision',
    'load arguments' => array(3),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('node_revision_revert_confirm', 1),
    'access callback' => '_node_revision_access',
    'access arguments' => array(1, 'update'),
    'file' => 'node.pages.inc',
  );
  $items['node/%node/revisions/%/delete'] = array(
    'title' => 'Delete earlier revision',
    'load arguments' => array(3),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('node_revision_delete_confirm', 1),
    'access callback' => '_node_revision_access',
    'access arguments' => array(1, 'delete'),
    'file' => 'node.pages.inc',
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
