# blog_page_last()

- **Type:** Function
- **File:** [`modules/blog/blog.pages.inc`](_file.md), lines 55–85 · [local source](../../../../source/modules/blog/blog.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.pages.inc#L55-L85)
- **Module/theme:** blog

## Signature

```php
function blog_page_last()
```

## Documentation

```text
Menu callback; displays a Drupal page containing recent blog entries of all users.
```

## Code

```php
function blog_page_last() {
  global $user;
  $build = array();

  $query = db_select('node', 'n')->extend('PagerDefault');
  $nids = $query
    ->fields('n', array('nid', 'sticky', 'created'))
    ->condition('type', 'blog')
    ->condition('status', 1)
    ->orderBy('sticky', 'DESC')
    ->orderBy('created', 'DESC')
    ->limit(variable_get('default_nodes_main', 10))
    ->addTag('node_access')
    ->execute()
    ->fetchCol();

  if (!empty($nids)) {
    $nodes = node_load_multiple($nids);
    $build += node_view_multiple($nodes);
    $build['pager'] = array(
      '#theme' => 'pager',
      '#weight' => 5,
    );
  }
  else {
    drupal_set_message(t('No blog entries have been created.'));
  }
  drupal_add_feed('blog/feed', t('RSS - blogs'));

  return $build;
}
```

---
_Drupal 7.103 · [modules/blog/blog.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
