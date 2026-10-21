# overlay_user_dismiss_message()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 328–343 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L328-L343)
- **Module/theme:** overlay

## Signature

```php
function overlay_user_dismiss_message()
```

## Documentation

```text
Page callback: Dismisses the overlay accessibility message for this user.

@return
  A render array for a page containing a list of content.
```

## Code

```php
function overlay_user_dismiss_message() {
  global $user;
  // It's unlikely, but possible that "access overlay" permission is granted to
  // the anonymous role. In this case, we do not display the message to disable
  // the overlay, so there is nothing to dismiss. Also, protect against
  // cross-site request forgeries by validating a token.
  if (empty($user->uid) || !isset($_GET['token']) || !drupal_valid_token($_GET['token'], 'overlay')) {
    return MENU_ACCESS_DENIED;
  }
  else {
    user_save(user_load($user->uid), array('data' => array('overlay_message_dismissed' => 1)));
    drupal_set_message(t('The message has been dismissed. You can change your overlay settings at any time by visiting your profile page.'));
    // Destination is normally given. Go to the user profile as a fallback.
    drupal_goto('user/' . $user->uid . '/edit');
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
