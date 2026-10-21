# book_outline_form()

- **Type:** Function
- **File:** [`modules/book/book.pages.inc`](_file.md), lines 132–166 · [local source](../../../../source/modules/book/book.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc#L132-L166)
- **Module/theme:** book
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function book_outline_form($form, &$form_state, $node)
```

## Documentation

```text
Form constructor for the book outline form.

Allows handling of all book outline operations via the outline tab.

@param $node
  The book node for which to show the outline.

@see book_outline_form_submit()
@see book_remove_button_submit()
@ingroup forms
```

## Code

```php
function book_outline_form($form, &$form_state, $node) {
  if (!isset($node->book)) {
    // The node is not part of any book yet - set default options.
    $node->book = _book_link_defaults($node->nid);
  }
  else {
    $node->book['original_bid'] = $node->book['bid'];
  }

  // Find the depth limit for the parent select.
  if (!isset($node->book['parent_depth_limit'])) {
    $node->book['parent_depth_limit'] = _book_parent_depth_limit($node->book);
  }
  $form['#node'] = $node;
  $form['#id'] = 'book-outline';
  _book_add_form_elements($form, $form_state, $node);

  $form['book']['#collapsible'] = FALSE;

  $form['update'] = array(
    '#type' => 'submit',
    '#value' => $node->book['original_bid'] ? t('Update book outline') : t('Add to book outline'),
    '#weight' => 15,
  );

  $form['remove'] = array(
    '#type' => 'submit',
    '#value' => t('Remove from book outline'),
    '#access' => _book_node_is_removable($node),
    '#weight' => 20,
    '#submit' => array('book_remove_button_submit'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/book/book.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
