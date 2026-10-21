# book_node_prepare()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 991–1018 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L991-L1018)
- **Module/theme:** book
- **Implements:** [hook_node_prepare()](../../node/node.api.php/hook_node_prepare.md)

## Signature

```php
function book_node_prepare($node)
```

## Documentation

```text
Implements hook_node_prepare().
```

## Code

```php
function book_node_prepare($node) {
  // Prepare defaults for the add/edit form.
  if (empty($node->book) && (user_access('add content to books') || user_access('administer book outlines'))) {
    $node->book = array();

    if (empty($node->nid) && isset($_GET['parent']) && is_numeric($_GET['parent'])) {
      // Handle "Add child page" links:
      $parent = book_link_load($_GET['parent']);

      if ($parent && $parent['access']) {
        $node->book['bid'] = $parent['bid'];
        $node->book['plid'] = $parent['mlid'];
        $node->book['menu_name'] = $parent['menu_name'];
      }
    }
    // Set defaults.
    $node->book += _book_link_defaults(!empty($node->nid) ? $node->nid : 'new');
  }
  else {
    if (isset($node->book['bid']) && !isset($node->book['original_bid'])) {
      $node->book['original_bid'] = $node->book['bid'];
    }
  }
  // Find the depth limit for the parent select.
  if (isset($node->book['bid']) && !isset($node->book['parent_depth_limit'])) {
    $node->book['parent_depth_limit'] = _book_parent_depth_limit($node->book);
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
