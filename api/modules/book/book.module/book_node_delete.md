# book_node_delete()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 967–986 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L967-L986)
- **Module/theme:** book
- **Implements:** [hook_node_delete()](../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function book_node_delete($node)
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function book_node_delete($node) {
  if (!empty($node->book['bid'])) {
    if ($node->nid == $node->book['bid']) {
      // Handle deletion of a top-level post.
      $result = db_query("SELECT b.nid FROM {menu_links} ml INNER JOIN {book} b on b.mlid = ml.mlid WHERE ml.plid = :plid", array(
        ':plid' => $node->book['mlid']
      ));
      foreach ($result as $child) {
        $child_node = node_load($child->nid);
        $child_node->book['bid'] = $child_node->nid;
        _book_update_outline($child_node);
      }
    }
    menu_link_delete($node->book['mlid']);
    db_delete('book')
      ->condition('mlid', $node->book['mlid'])
      ->execute();
    drupal_static_reset('book_get_books');
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
