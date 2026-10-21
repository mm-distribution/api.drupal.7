# book_export_traverse()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1243–1266 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1243-L1266)
- **Module/theme:** book

## Signature

```php
function book_export_traverse($tree, $visit_func)
```

## Documentation

```text
Traverses the book tree to build printable or exportable output.

During the traversal, the $visit_func() callback is applied to each node and
is called recursively for each child of the node (in weight, title order).

@param $tree
  A subtree of the book menu hierarchy, rooted at the current page.
@param $visit_func
  A function callback to be called upon visiting a node in the tree.

@return
  The output generated in visiting each node.
```

## Code

```php
function book_export_traverse($tree, $visit_func) {
  $output = '';

  foreach ($tree as $data) {
    // Note- access checking is already performed when building the tree.
    if ($node = node_load($data['link']['nid'], FALSE)) {
      $children = '';

      if ($data['below']) {
        $children = book_export_traverse($data['below'], $visit_func);
      }

      if (function_exists($visit_func)) {
        $output .= call_user_func($visit_func, $node, $children);
      }
      else {
        // Use the default function.
        $output .= book_node_export($node, $children);
      }
    }
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
