# book_admin_edit_validate()

- **Type:** Function
- **File:** [`modules/book/book.admin.inc`](_file.md), lines 102–106 · [local source](../../../../source/modules/book/book.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc#L102-L106)
- **Module/theme:** book

## Signature

```php
function book_admin_edit_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for book_admin_edit().

Checks that the book has not been changed while using the form.

@see book_admin_edit_submit()
```

## Code

```php
function book_admin_edit_validate($form, &$form_state) {
  if ($form_state['values']['tree_hash'] != $form_state['values']['tree_current_hash']) {
    form_set_error('', t('This book has been modified by another user, the changes could not be saved.'));
  }
}
```

---
_Drupal 7.103 · [modules/book/book.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
