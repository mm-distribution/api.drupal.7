# user_multiple_cancel_confirm_submit()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3454–3476 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3454-L3476)
- **Module/theme:** user

## Signature

```php
function user_multiple_cancel_confirm_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for mass-account cancellation form.

@see user_multiple_cancel_confirm()
@see user_cancel_confirm_form_submit()
```

## Code

```php
function user_multiple_cancel_confirm_submit($form, &$form_state) {
  global $user;

  if ($form_state['values']['confirm']) {
    foreach ($form_state['values']['accounts'] as $uid => $value) {
      // Prevent programmatic form submissions from cancelling user 1.
      if ($uid <= 1) {
        continue;
      }
      // Prevent user administrators from deleting themselves without confirmation.
      if ($uid == $user->uid) {
        $admin_form_state = $form_state;
        unset($admin_form_state['values']['user_cancel_confirm']);
        $admin_form_state['values']['_account'] = $user;
        user_cancel_confirm_form_submit(array(), $admin_form_state);
      }
      else {
        user_cancel($form_state['values'], $uid, $form_state['values']['user_cancel_method']);
      }
    }
  }
  $form_state['redirect'] = 'admin/people';
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
