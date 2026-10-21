# contact_personal_form_validate()

- **Type:** Function
- **File:** [`modules/contact/contact.pages.inc`](_file.md), lines 258–262 · [local source](../../../../source/modules/contact/contact.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.pages.inc#L258-L262)
- **Module/theme:** contact

## Signature

```php
function contact_personal_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for contact_personal_form().

@see contact_personal_form_submit()
```

## Code

```php
function contact_personal_form_validate($form, &$form_state) {
  if (!valid_email_address($form_state['values']['mail'])) {
    form_set_error('mail', t('You must enter a valid e-mail address.'));
  }
}
```

---
_Drupal 7.103 · [modules/contact/contact.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
