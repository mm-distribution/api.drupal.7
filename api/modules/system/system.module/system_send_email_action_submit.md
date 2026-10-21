# system_send_email_action_submit()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3250–3260 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3250-L3260)
- **Module/theme:** system

## Signature

```php
function system_send_email_action_submit($form, $form_state)
```

## Documentation

```text
Process system_send_email_action form submissions.
```

## Code

```php
function system_send_email_action_submit($form, $form_state) {
  $form_values = $form_state['values'];
  // Process the HTML form to store configuration. The keyed array that
  // we return will be serialized to the database.
  $params = array(
    'recipient' => $form_values['recipient'],
    'subject'   => $form_values['subject'],
    'message'   => $form_values['message'],
  );
  return $params;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
