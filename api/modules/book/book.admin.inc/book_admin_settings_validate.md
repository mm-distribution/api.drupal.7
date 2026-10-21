# book_admin_settings_validate()

- **Type:** Function
- **File:** [`modules/book/book.admin.inc`](_file.md), lines 64–69 · [local source](../../../../source/modules/book/book.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc#L64-L69)
- **Module/theme:** book

## Signature

```php
function book_admin_settings_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for book_admin_settings().

@see book_admin_settings_submit()
```

## Code

```php
function book_admin_settings_validate($form, &$form_state) {
  $child_type = $form_state['values']['book_child_type'];
  if (empty($form_state['values']['book_allowed_types'][$child_type])) {
    form_set_error('book_child_type', t('The content type for the %add-child link must be one of those selected as an allowed book outline type.', array('%add-child' => t('Add child page'))));
  }
}
```

---
_Drupal 7.103 · [modules/book/book.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
