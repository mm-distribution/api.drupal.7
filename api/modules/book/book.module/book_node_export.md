# book_node_export()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1282–1289 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1282-L1289)
- **Module/theme:** book

## Signature

```php
function book_node_export($node, $children = '')
```

## Documentation

```text
Generates printer-friendly HTML for a node.

@param $node
  The node that will be output.
@param $children
  (optional) All the rendered child nodes within the current node. Defaults
  to an empty string.

@return
  The HTML generated for the given node.

@see book_export_traverse()
```

## Code

```php
function book_node_export($node, $children = '') {
  $build = node_view($node, 'print');
  unset($build['#theme']);
  // @todo Rendering should happen in the template using render().
  $node->rendered = drupal_render($build);

  return theme('book_node_export_html', array('node' => $node, 'children' => $children));
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
