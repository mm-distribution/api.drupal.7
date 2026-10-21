# forum_node_view()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 265–283 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L265-L283)
- **Module/theme:** forum
- **Implements:** [hook_node_view()](../../node/node.api.php/hook_node_view.md)

## Signature

```php
function forum_node_view($node, $view_mode)
```

## Documentation

```text
Implements hook_node_view().
```

## Code

```php
function forum_node_view($node, $view_mode) {
  if (!empty($node->forum_tid) && _forum_node_check_node_type($node)) {
    if ($view_mode == 'full' && node_is_page($node)) {
      $vid = variable_get('forum_nav_vocabulary', 0);
      $vocabulary = taxonomy_vocabulary_load($vid);
      // Breadcrumb navigation
      $breadcrumb[] = l(t('Home'), NULL);
      $breadcrumb[] = l($vocabulary->name, 'forum');
      if ($parents = taxonomy_get_parents_all($node->forum_tid)) {
        $parents = array_reverse($parents);
        foreach ($parents as $parent) {
          $breadcrumb[] = l($parent->name, 'forum/' . $parent->tid);
        }
      }
      drupal_set_breadcrumb($breadcrumb);

    }
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
