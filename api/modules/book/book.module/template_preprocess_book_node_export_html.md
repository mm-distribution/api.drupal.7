# template_preprocess_book_node_export_html()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1301–1305 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1301-L1305)
- **Module/theme:** book

## Signature

```php
function template_preprocess_book_node_export_html(&$variables)
```

## Documentation

```text
Processes variables for book-node-export-html.tpl.php.

@param $variables
  An associative array containing the following keys:
  - node
  - children

@see book-node-export-html.tpl.php
```

## Code

```php
function template_preprocess_book_node_export_html(&$variables) {
  $variables['depth'] = $variables['node']->book['depth'];
  $variables['title'] = check_plain($variables['node']->title);
  $variables['content'] = $variables['node']->rendered;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
