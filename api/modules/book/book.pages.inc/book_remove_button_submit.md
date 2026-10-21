# book_remove_button_submit()

- **Type:** Function
- **File:** [`modules/book/book.pages.inc`](_file.md), lines 175–177 · [local source](../../../../source/modules/book/book.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc#L175-L177)
- **Module/theme:** book

## Signature

```php
function book_remove_button_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for book_outline_form().

Redirects to removal confirmation form.

@see book_outline_form_submit()
```

## Code

```php
function book_remove_button_submit($form, &$form_state) {
  $form_state['redirect'] = 'node/' . $form['#node']->nid . '/outline/remove';
}
```

---
_Drupal 7.103 · [modules/book/book.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
