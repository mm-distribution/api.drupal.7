# _book_admin_table()

- **Type:** Function
- **File:** [`modules/book/book.admin.inc`](_file.md), lines 163–186 · [local source](../../../../source/modules/book/book.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc#L163-L186)
- **Module/theme:** book

## Signature

```php
function _book_admin_table($node, &$form)
```

## Documentation

```text
Builds the table portion of the form for the book administration page.

@param $node
  The node of the top-level page in the book.
@param $form
  The form that is being modified, passed by reference.

@see book_admin_edit()
```

## Code

```php
function _book_admin_table($node, &$form) {
  $form['table'] = array(
    '#theme' => 'book_admin_table',
    '#tree' => TRUE,
  );

  $tree = book_menu_subtree_data($node->book);
  $tree = array_shift($tree); // Do not include the book item itself.
  if ($tree['below']) {
    $hash = drupal_hash_base64(serialize($tree['below']));
    // Store the hash value as a hidden form element so that we can detect
    // if another user changed the book hierarchy.
    $form['tree_hash'] = array(
      '#type' => 'hidden',
      '#default_value' => $hash,
    );
    $form['tree_current_hash'] = array(
      '#type' => 'value',
      '#value' => $hash,
    );
    _book_admin_table_tree($tree['below'], $form['table']);
  }

}
```

---
_Drupal 7.103 · [modules/book/book.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
