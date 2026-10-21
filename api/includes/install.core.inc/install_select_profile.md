# install_select_profile()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1052–1077 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1052-L1077)

## Signature

```php
function install_select_profile(&$install_state)
```

## Documentation

```text
Selects which profile to install.

@param $install_state
  An array of information about the current installation state. The chosen
  profile will be added here, if it was not already selected previously, as
  will a list of all available profiles.

@return
  For interactive installations, a form allowing the profile to be selected,
  if the user has a choice that needs to be made. Otherwise, an exception is
  thrown if a profile cannot be chosen automatically.
```

## Code

```php
function install_select_profile(&$install_state) {
  $install_state['profiles'] += install_find_profiles();
  if (empty($install_state['parameters']['profile'])) {
    // Try to find a profile.
    $profile = _install_select_profile($install_state['profiles']);
    if (empty($profile)) {
      // We still don't have a profile, so display a form for selecting one.
      // Only do this in the case of interactive installations, since this is
      // not a real form with submit handlers (the database isn't even set up
      // yet), rather just a convenience method for setting parameters in the
      // URL.
      if ($install_state['interactive']) {
        include_once DRUPAL_ROOT . '/includes/form.inc';
        drupal_set_title(st('Select an installation profile'));
        $form = drupal_get_form('install_select_profile_form', $install_state['profiles']);
        return drupal_render($form);
      }
      else {
        throw new Exception(install_no_profile_error());
      }
    }
    else {
      $install_state['parameters']['profile'] = $profile;
    }
  }
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
