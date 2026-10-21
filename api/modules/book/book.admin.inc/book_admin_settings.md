# book_admin_settings()

- **Type:** Function
- **File:** [`modules/book/book.admin.inc`](_file.md), lines 36–57 · [local source](../../../../source/modules/book/book.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc#L36-L57)
- **Module/theme:** book
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function book_admin_settings()
```

## Documentation

```text
Form constructor for the book settings form.

@see book_admin_settings_validate()

@ingroup forms
```

## Code

```php
function book_admin_settings() {
  $types = node_type_get_names();
  $form['book_allowed_types'] = array(
    '#type' => 'checkboxes',
    '#title' => t('Content types allowed in book outlines'),
    '#default_value' => variable_get('book_allowed_types', array('book')),
    '#options' => $types,
    '#description' => t('Users with the %outline-perm permission can add all content types.', array('%outline-perm' => t('Administer book outlines'))),
    '#required' => TRUE,
  );
  $form['book_child_type'] = array(
    '#type' => 'radios',
    '#title' => t('Content type for child pages'),
    '#default_value' => variable_get('book_child_type', 'book'),
    '#options' => $types,
    '#required' => TRUE,
  );
  $form['array_filter'] = array('#type' => 'value', '#value' => TRUE);
  $form['#validate'][] = 'book_admin_settings_validate';

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/book/book.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
