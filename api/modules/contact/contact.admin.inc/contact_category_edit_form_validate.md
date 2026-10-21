# contact_category_edit_form_validate()

- **Type:** Function
- **File:** [`modules/contact/contact.admin.inc`](_file.md), lines 139–161 · [local source](../../../../source/modules/contact/contact.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc#L139-L161)
- **Module/theme:** contact

## Signature

```php
function contact_category_edit_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for contact_category_edit_form().

@see contact_category_edit_form_submit()
```

## Code

```php
function contact_category_edit_form_validate($form, &$form_state) {
  // Validate and each e-mail recipient.
  $recipients = explode(',', $form_state['values']['recipients']);

  // When creating a new contact form, or renaming the category on an existing
  // contact form, make sure that the given category is unique.
  $category = $form_state['values']['category'];
  $query = db_select('contact', 'c')->condition('c.category', $category, '=');
  if (!empty($form_state['values']['cid'])) {
    $query->condition('c.cid', $form_state['values']['cid'], '<>');
  }
  if ($query->countQuery()->execute()->fetchField()) {
    form_set_error('category', t('A contact form with category %category already exists.', array('%category' => $category)));
  }

  foreach ($recipients as &$recipient) {
    $recipient = trim($recipient);
    if (!valid_email_address($recipient)) {
      form_set_error('recipients', t('%recipient is an invalid e-mail address.', array('%recipient' => $recipient)));
    }
  }
  $form_state['values']['recipients'] = implode(',', $recipients);
}
```

---
_Drupal 7.103 · [modules/contact/contact.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
