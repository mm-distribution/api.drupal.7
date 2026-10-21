# shortcut_set_switch_submit()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 125–164 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L125-L164)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_switch_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for shortcut_set_switch().
```

## Code

```php
function shortcut_set_switch_submit($form, &$form_state) {
  global $user;
  $account = $form_state['values']['account'];

  if ($form_state['values']['set'] == 'new') {
    // Save a new shortcut set with links copied from the user's default set.
    $default_set = shortcut_default_set($account);
    $set = (object) array(
      'title' => $form_state['values']['new'],
      'links' => menu_links_clone($default_set->links),
    );
    shortcut_set_save($set);
    $replacements = array(
      '%user' => $account->name,
      '%set_name' => $set->title,
      '@switch-url' => url(current_path()),
    );
    if ($account->uid == $user->uid) {
      // Only administrators can create new shortcut sets, so we know they have
      // access to switch back.
      drupal_set_message(t('You are now using the new %set_name shortcut set. You can edit it from this page or <a href="@switch-url">switch back to a different one.</a>', $replacements));
    }
    else {
      drupal_set_message(t('%user is now using a new shortcut set called %set_name. You can edit it from this page.', $replacements));
    }
    $form_state['redirect'] = 'admin/config/user-interface/shortcut/' . $set->set_name;
  }
  else {
    // Switch to a different shortcut set.
    $set = shortcut_set_load($form_state['values']['set']);
    $replacements = array(
      '%user' => $account->name,
      '%set_name' => $set->title,
    );
    drupal_set_message($account->uid == $user->uid ? t('You are now using the %set_name shortcut set.', $replacements) : t('%user is now using the %set_name shortcut set.', $replacements));
  }

  // Assign the shortcut set to the provided user account.
  shortcut_set_assign_user($set, $account);
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
