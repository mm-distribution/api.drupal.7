# contact_category_delete_form_submit()

- **Type:** Function
- **File:** [`modules/contact/contact.admin.inc`](_file.md), lines 217–228 · [local source](../../../../source/modules/contact/contact.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc#L217-L228)
- **Module/theme:** contact

## Signature

```php
function contact_category_delete_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for contact_category_delete_form().
```

## Code

```php
function contact_category_delete_form_submit($form, &$form_state) {
  $contact = $form['contact']['#value'];

  db_delete('contact')
    ->condition('cid', $contact['cid'])
    ->execute();

  drupal_set_message(t('Category %category has been deleted.', array('%category' => $contact['category'])));
  watchdog('contact', 'Category %category has been deleted.', array('%category' => $contact['category']), WATCHDOG_NOTICE);

  $form_state['redirect'] = 'admin/structure/contact';
}
```

---
_Drupal 7.103 · [modules/contact/contact.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
