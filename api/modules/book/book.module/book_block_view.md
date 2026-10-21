# book_block_view()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 275–324 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L275-L324)
- **Module/theme:** book
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function book_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().

Displays the book table of contents in a block when the current page is a
single-node view of a book node.
```

## Code

```php
function book_block_view($delta = '') {
  $block = array();
  $current_bid = 0;
  if ($node = menu_get_object()) {
    $current_bid = empty($node->book['bid']) ? 0 : $node->book['bid'];
  }

  if (variable_get('book_block_mode', 'all pages') == 'all pages') {
    $block['subject'] = t('Book navigation');
    $book_menus = array();
    $pseudo_tree = array(0 => array('below' => FALSE));
    foreach (book_get_books() as $book_id => $book) {
      if ($book['bid'] == $current_bid) {
        // If the current page is a node associated with a book, the menu
        // needs to be retrieved.
        $book_menus[$book_id] = menu_tree_output(menu_tree_all_data($node->book['menu_name'], $node->book));
      }
      else {
        // Since we know we will only display a link to the top node, there
        // is no reason to run an additional menu tree query for each book.
        $book['in_active_trail'] = FALSE;
        // Check whether user can access the book link.
        $book_node = node_load($book['nid']);
        $book['access'] = node_access('view', $book_node);
        $pseudo_tree[0]['link'] = $book;
        $book_menus[$book_id] = menu_tree_output($pseudo_tree);
      }
    }
    $book_menus['#theme'] = 'book_all_books_block';
    $block['content'] = $book_menus;
  }
  elseif ($current_bid) {
    // Only display this block when the user is browsing a book.
  $select = db_select('node', 'n')
    ->fields('n', array('title'))
    ->condition('n.nid', $node->book['bid'])
    ->addTag('node_access');
    $title = $select->execute()->fetchField();
    // Only show the block if the user has view access for the top-level node.
    if ($title) {
      $tree = menu_tree_all_data($node->book['menu_name'], $node->book);
      // There should only be one element at the top level.
      $data = array_shift($tree);
      $block['subject'] = theme('book_title_link', array('link' => $data['link']));
      $block['content'] = ($data['below']) ? menu_tree_output($data['below']) : '';
    }
  }

  return $block;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
