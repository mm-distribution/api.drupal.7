# book_outline_form_submit()

- **Type:** Function
- **File:** [`modules/book/book.pages.inc`](_file.md), lines 184–209 · [local source](../../../../source/modules/book/book.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc#L184-L209)
- **Module/theme:** book

## Signature

```php
function book_outline_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for book_outline_form().

@see book_remove_button_submit()
```

## Code

```php
function book_outline_form_submit($form, &$form_state) {
  $node = $form['#node'];
  $form_state['redirect'] = "node/" . $node->nid;
  $book_link = $form_state['values']['book'];
  if (!$book_link['bid']) {
    drupal_set_message(t('No changes were made'));

    return;
  }

  $book_link['menu_name'] = book_menu_name($book_link['bid']);
  $node->book = $book_link;
  if (_book_update_outline($node)) {
    if ($node->book['parent_mismatch']) {
      // This will usually only happen when JS is disabled.
      drupal_set_message(t('The post has been added to the selected book. You may now position it relative to other pages.'));
      $form_state['redirect'] = "node/" . $node->nid . "/outline";
    }
    else {
      drupal_set_message(t('The book outline has been updated.'));
    }
  }
  else {
    drupal_set_message(t('There was an error adding the post to the book.'), 'error');
  }
}
```

---
_Drupal 7.103 · [modules/book/book.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
