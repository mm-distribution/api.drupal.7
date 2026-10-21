# book_form_node_delete_confirm_alter()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1040–1049 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1040-L1049)
- **Module/theme:** book
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function book_form_node_delete_confirm_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() for node_delete_confirm().

Alters the confirm form for a single node deletion.

@see node_delete_confirm()
```

## Code

```php
function book_form_node_delete_confirm_alter(&$form, $form_state) {
  $node = node_load($form['nid']['#value']);

  if (isset($node->book) && $node->book['has_children']) {
    $form['book_warning'] = array(
      '#markup' => '<p>' . t('%title is part of a book outline, and has associated child pages. If you proceed with deletion, the child pages will be relocated automatically.', array('%title' => $node->title)) . '</p>',
      '#weight' => -10,
    );
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
