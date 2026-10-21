# book_node_view()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 887–900 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L887-L900)
- **Module/theme:** book
- **Implements:** [hook_node_view()](../../node/node.api.php/hook_node_view.md)

## Signature

```php
function book_node_view($node, $view_mode)
```

## Documentation

```text
Implements hook_node_view().
```

## Code

```php
function book_node_view($node, $view_mode) {
  if ($view_mode == 'full') {
    if (!empty($node->book['bid']) && empty($node->in_preview)) {
      $node->content['book_navigation'] = array(
        '#markup' => theme('book_navigation', array('book_link' => $node->book)),
        '#weight' => 100,
      );
    }
  }

  if ($view_mode != 'rss') {
    book_node_view_link($node, $view_mode);
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
