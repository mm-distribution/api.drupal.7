# overlay_disable_message()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 358–406 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L358-L406)
- **Module/theme:** overlay

## Signature

```php
function overlay_disable_message()
```

## Documentation

```text
Returns a renderable array representing a message for disabling the overlay.

If the current user can access the overlay and has not previously indicated
that this message should be dismissed, this function returns a message
containing a link to disable the overlay. Nothing is returned for anonymous
users, because the links control per-user settings. Because some screen
readers are unable to properly read overlay contents, site builders are
discouraged from granting the "access overlay" permission to the anonymous
role.

@see http://drupal.org/node/890284
```

## Code

```php
function overlay_disable_message() {
  global $user;

  if (!empty($user->uid) && empty($user->data['overlay_message_dismissed']) && (!isset($user->data['overlay']) || $user->data['overlay']) && user_access('access overlay')) {
    $build = array(
      '#theme' => 'overlay_disable_message',
      '#weight' => -99,
      // Link to the user's profile page, where the overlay can be disabled.
      'profile_link' => array(
        '#type' => 'link',
        '#title' => t('If you have problems accessing administrative pages on this site, disable the overlay on your profile page.'),
        '#href' => 'user/' . $user->uid . '/edit',
        '#options' => array(
          'query' => drupal_get_destination(),
          'fragment' => 'edit-overlay-control',
          'attributes' => array(
            'id' => 'overlay-profile-link',
            // Prevent the target page from being opened in the overlay.
            'class' => array('overlay-exclude'),
          ),
        ),
      ),
      // Link to a menu callback that allows this message to be permanently
      // dismissed for the current user.
      'dismiss_message_link' => array(
        '#type' => 'link',
        '#title' => t('Dismiss this message.'),
        '#href' => 'overlay/dismiss-message',
        '#options' => array(
          'query' => drupal_get_destination() + array(
            // Add a token to protect against cross-site request forgeries.
            'token' => drupal_get_token('overlay'),
          ),
          'attributes' => array(
            'id' => 'overlay-dismiss-message',
            // If this message is being displayed outside the overlay, prevent
            // this link from opening the overlay.
            'class' => (overlay_get_mode() == 'parent') ? array('overlay-exclude') : array(),
          ),
        ),
      )
    );
  }
  else {
    $build = array();
  }

  return $build;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
