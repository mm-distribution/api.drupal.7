# book_form_node_form_alter()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 419–441 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L419-L441)
- **Module/theme:** book
- **Implements:** [hook_form_BASE_FORM_ID_alter()](../../system/system.api.php/hook_form_BASE_FORM_ID_alter.md)

## Signature

```php
function book_form_node_form_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Implements hook_form_BASE_FORM_ID_alter() for node_form().

Adds the book fieldset to the node form.

@see book_pick_book_nojs_submit()
```

## Code

```php
function book_form_node_form_alter(&$form, &$form_state, $form_id) {
  $node = $form['#node'];
  $access = user_access('administer book outlines');
  if (!$access) {
    if (user_access('add content to books') && ((!empty($node->book['mlid']) && !empty($node->nid)) || book_type_is_allowed($node->type))) {
      // Already in the book hierarchy, or this node type is allowed.
      $access = TRUE;
    }
  }

  if ($access) {
    _book_add_form_elements($form, $form_state, $node);
    // Since the "Book" dropdown can't trigger a form submission when
    // JavaScript is disabled, add a submit button to do that. book.css hides
    // this button when JavaScript is enabled.
    $form['book']['pick-book'] = array(
      '#type' => 'submit',
      '#value' => t('Change book (update list of parents)'),
      '#submit' => array('book_pick_book_nojs_submit'),
      '#weight' => 20,
    );
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
