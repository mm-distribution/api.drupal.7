# book_node_view_link()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 94–125 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L94-L125)
- **Module/theme:** book

## Signature

```php
function book_node_view_link($node, $view_mode)
```

## Documentation

```text
Adds relevant book links to the node's links.

@param $node
  The book page node to add links to.
@param $view_mode
  The view mode of the node.
```

## Code

```php
function book_node_view_link($node, $view_mode) {
  $links = array();

  if (isset($node->book['depth'])) {
    if ($view_mode == 'full' && node_is_page($node)) {
      $child_type = variable_get('book_child_type', 'book');
      if ((user_access('add content to books') || user_access('administer book outlines')) && node_access('create', $child_type) && $node->status == 1 && $node->book['depth'] < MENU_MAX_DEPTH) {
        $links['book_add_child'] = array(
          'title' => t('Add child page'),
          'href' => 'node/add/' . str_replace('_', '-', $child_type),
          'query' => array('parent' => $node->book['mlid']),
        );
      }

      if (user_access('access printer-friendly version')) {
        $links['book_printer'] = array(
          'title' => t('Printer-friendly version'),
          'href' => 'book/export/html/' . $node->nid,
          'attributes' => array('title' => t('Show a printer-friendly version of this book page and its sub-pages.'))
        );
      }
    }
  }

  if (!empty($links)) {
    $node->content['links']['book'] = array(
      '#theme' => 'links__node__book',
      '#links' => $links,
      '#attributes' => array('class' => array('links', 'inline')),
    );
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
