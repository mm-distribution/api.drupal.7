# book_remove_form_submit()

- **Type:** Function
- **File:** [`modules/book/book.pages.inc`](_file.md), lines 237–247 · [local source](../../../../source/modules/book/book.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc#L237-L247)
- **Module/theme:** book

## Signature

```php
function book_remove_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for book_remove_form().
```

## Code

```php
function book_remove_form_submit($form, &$form_state) {
  $node = $form['#node'];
  if (_book_node_is_removable($node)) {
    menu_link_delete($node->book['mlid']);
    db_delete('book')
      ->condition('nid', $node->nid)
      ->execute();
    drupal_set_message(t('The post has been removed from the book.'));
  }
  $form_state['redirect'] = 'node/' . $node->nid;
}
```

---
_Drupal 7.103 · [modules/book/book.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
