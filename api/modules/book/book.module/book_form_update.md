# book_form_update()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 609–611 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L609-L611)
- **Module/theme:** book

## Signature

```php
function book_form_update($form, $form_state)
```

## Documentation

```text
Renders a new parent page select element when the book selection changes.

This function is called via Ajax when the selected book is changed on a node
or book outline form.

@return
  The rendered parent page select element.
```

## Code

```php
function book_form_update($form, $form_state) {
  return $form['book']['plid'];
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
