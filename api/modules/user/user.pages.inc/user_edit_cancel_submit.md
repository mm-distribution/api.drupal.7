# user_edit_cancel_submit()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 483–491 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L483-L491)
- **Module/theme:** user

## Signature

```php
function user_edit_cancel_submit($form, &$form_state)
```

## Documentation

```text
Submit function for the 'Cancel account' button on the user edit form.
```

## Code

```php
function user_edit_cancel_submit($form, &$form_state) {
  $destination = array();
  if (isset($_GET['destination'])) {
    $destination = drupal_get_destination();
    unset($_GET['destination']);
  }
  // Note: We redirect from user/uid/edit to user/uid/cancel to make the tabs disappear.
  $form_state['redirect'] = array("user/" . $form['#user']->uid . "/cancel", array('query' => $destination));
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
