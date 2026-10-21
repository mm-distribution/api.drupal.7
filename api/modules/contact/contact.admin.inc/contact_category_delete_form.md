# contact_category_delete_form()

- **Type:** Function
- **File:** [`modules/contact/contact.admin.inc`](_file.md), lines 198–212 · [local source](../../../../source/modules/contact/contact.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc#L198-L212)
- **Module/theme:** contact

## Signature

```php
function contact_category_delete_form($form, &$form_state, array $contact)
```

## Documentation

```text
Form constructor for the contact category deletion form.

@param $contact
  Array describing the contact category to be deleted. See the documentation
  of contact_category_edit_form() for the recognized keys.

@see contact_menu()
@see contact_category_delete_form_submit()
```

## Code

```php
function contact_category_delete_form($form, &$form_state, array $contact) {
  $form['contact'] = array(
    '#type' => 'value',
    '#value' => $contact,
  );

  return confirm_form(
    $form,
    t('Are you sure you want to delete %category?', array('%category' => $contact['category'])),
    'admin/structure/contact',
    t('This action cannot be undone.'),
    t('Delete'),
    t('Cancel')
  );
}
```

---
_Drupal 7.103 · [modules/contact/contact.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
