# _install_select_profile()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1096–1131 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1096-L1131)

## Signature

```php
function _install_select_profile($profiles)
```

## Documentation

```text
Selects an installation profile.

A profile will be selected if:
- Only one profile is available,
- A profile was submitted through $_POST,
- Exactly one of the profiles is marked as "exclusive".
If multiple profiles are marked as "exclusive" then no profile will be
selected.

@param array $profiles
  An associative array of profiles with the machine-readable names as keys.

@return
  The machine-readable name of the selected profile or NULL if no profile was
  selected.
```

## Code

```php
function _install_select_profile($profiles) {
  if (sizeof($profiles) == 0) {
    throw new Exception(install_no_profile_error());
  }
  // Don't need to choose profile if only one available.
  if (sizeof($profiles) == 1) {
    $profile = array_pop($profiles);
    // TODO: is this right?
    require_once DRUPAL_ROOT . '/' . $profile->uri;
    return $profile->name;
  }
  else {
    foreach ($profiles as $profile) {
      if (!empty($_POST['profile']) && ($_POST['profile'] == $profile->name)) {
        return $profile->name;
      }
    }
  }
  // Check for a profile marked as "exclusive" and ensure that only one
  // profile is marked as such.
  $exclusive_profile = NULL;
  foreach ($profiles as $profile) {
    $profile_info = install_profile_info($profile->name);
    if (!empty($profile_info['exclusive'])) {
      if (empty($exclusive_profile)) {
        $exclusive_profile = $profile->name;
      }
      else {
        // We found a second "exclusive" profile. There's no way to choose
        // between them, so we ignore the property.
        return;
      }
    }
  }
  return $exclusive_profile;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
