# book_pick_book_nojs_submit()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 455–458 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L455-L458)
- **Module/theme:** book

## Signature

```php
function book_pick_book_nojs_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for node_form().

This handler is run when JavaScript is disabled. It triggers the form to
rebuild so that the "Parent item" options are changed to reflect the newly
selected book. When JavaScript is enabled, the submit button that triggers
this handler is hidden, and the "Book" dropdown directly triggers the
book_form_update() Ajax callback instead.

@see book_form_update()
@see book_form_node_form_alter()
```

## Code

```php
function book_pick_book_nojs_submit($form, &$form_state) {
  $form_state['node']->book = $form_state['values']['book'];
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
