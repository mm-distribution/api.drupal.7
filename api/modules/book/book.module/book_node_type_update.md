# book_node_type_update()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1326–1343 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1326-L1343)
- **Module/theme:** book
- **Implements:** [hook_node_type_update()](../../node/node.api.php/hook_node_type_update.md)

## Signature

```php
function book_node_type_update($type)
```

## Documentation

```text
Implements hook_node_type_update().

Updates the Book module's persistent variables if the machine-readable name
of a node type is changed.
```

## Code

```php
function book_node_type_update($type) {
  if (!empty($type->old_type) && $type->old_type != $type->type) {
    // Update the list of node types that are allowed to be added to books.
    $allowed_types = variable_get('book_allowed_types', array('book'));
    $key = array_search($type->old_type, $allowed_types);

    if ($key !== FALSE) {
      $allowed_types[$type->type] = $allowed_types[$key] ? $type->type : 0;
      unset($allowed_types[$key]);
      variable_set('book_allowed_types', $allowed_types);
    }

    // Update the setting for the "Add child page" link.
    if (variable_get('book_child_type', 'book') == $type->old_type) {
      variable_set('book_child_type', $type->type);
    }
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
