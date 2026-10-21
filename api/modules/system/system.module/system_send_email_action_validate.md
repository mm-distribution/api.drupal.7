# system_send_email_action_validate()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3238–3245 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3238-L3245)
- **Module/theme:** system

## Signature

```php
function system_send_email_action_validate($form, $form_state)
```

## Documentation

```text
Validate system_send_email_action form submissions.
```

## Code

```php
function system_send_email_action_validate($form, $form_state) {
  $form_values = $form_state['values'];
  // Validate the configuration form.
  if (!valid_email_address($form_values['recipient']) && strpos($form_values['recipient'], ':mail') === FALSE) {
    // We want the literal %author placeholder to be emphasized in the error message.
    form_set_error('recipient', t('Enter a valid email address or use a token e-mail address such as %author.', array('%author' => '[node:author:mail]')));
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
