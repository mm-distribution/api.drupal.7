# node_page_default()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2693–2738 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2693-L2738)
- **Module/theme:** node

## Signature

```php
function node_page_default()
```

## Documentation

```text
Menu callback: Generates a listing of promoted nodes.

@return array
  An array in the format expected by drupal_render().

@see node_menu()
```

## Code

```php
function node_page_default() {
  $select = db_select('node', 'n')
    ->fields('n', array('nid', 'sticky', 'created'))
    ->condition('n.promote', 1)
    ->condition('n.status', 1)
    ->orderBy('n.sticky', 'DESC')
    ->orderBy('n.created', 'DESC')
    ->extend('PagerDefault')
    ->limit(variable_get('default_nodes_main', 10))
    ->addTag('node_access');

  $nids = $select->execute()->fetchCol();

  if (!empty($nids)) {
    $nodes = node_load_multiple($nids);
    $build = node_view_multiple($nodes);

    // 'rss.xml' is a path, not a file, registered in node_menu().
    drupal_add_feed('rss.xml', variable_get('site_name', 'Drupal') . ' ' . t('RSS'));
    $build['pager'] = array(
      '#theme' => 'pager',
      '#weight' => 5,
    );
    drupal_set_title('');
  }
  else {
    drupal_set_title(t('Welcome to @site-name', array('@site-name' => variable_get('site_name', 'Drupal'))), PASS_THROUGH);

    $default_message = '<p>' . t('No front page content has been created yet.') . '</p>';

    $default_links = array();
    if (_node_add_access()) {
      $default_links[] = l(t('Add new content'), 'node/add');
    }
    if (!empty($default_links)) {
      $default_message .= theme('item_list', array('items' => $default_links));
    }

    $build['default_message'] = array(
      '#markup' => $default_message,
      '#prefix' => '<div id="first-time">',
      '#suffix' => '</div>',
    );
  }
  return $build;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
