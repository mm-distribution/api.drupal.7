# contact_category_edit_form_submit()

- **Type:** Function
- **File:** [`modules/contact/contact.admin.inc`](_file.md), lines 168–186 · [local source](../../../../source/modules/contact/contact.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc#L168-L186)
- **Module/theme:** contact

## Signature

```php
function contact_category_edit_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for contact_category_edit_form().

@see contact_category_edit_form_validate()
```

## Code

```php
function contact_category_edit_form_submit($form, &$form_state) {
  if ($form_state['values']['selected']) {
    // Unselect all other contact categories.
    db_update('contact')
      ->fields(array('selected' => '0'))
      ->execute();
  }

  if (empty($form_state['values']['cid'])) {
    drupal_write_record('contact', $form_state['values']);
  }
  else {
    drupal_write_record('contact', $form_state['values'], array('cid'));
  }

  drupal_set_message(t('Category %category has been saved.', array('%category' => $form_state['values']['category'])));
  watchdog('contact', 'Category %category has been saved.', array('%category' => $form_state['values']['category']), WATCHDOG_NOTICE, l(t('Edit'), 'admin/structure/contact/edit/' . $form_state['values']['cid']));
  $form_state['redirect'] = 'admin/structure/contact';
}
```

---
_Drupal 7.103 · [modules/contact/contact.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
