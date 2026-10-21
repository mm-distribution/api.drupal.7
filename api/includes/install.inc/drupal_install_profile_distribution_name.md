# drupal_install_profile_distribution_name()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 196–209 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L196-L209)

## Signature

```php
function drupal_install_profile_distribution_name()
```

## Documentation

```text
Loads the installation profile, extracting its defined distribution name.

@return
  The distribution name defined in the profile's .info file. Defaults to
  "Drupal" if none is explicitly provided by the installation profile.

@see install_profile_info()
```

## Code

```php
function drupal_install_profile_distribution_name() {
  // During installation, the profile information is stored in the global
  // installation state (it might not be saved anywhere yet).
  if (drupal_installation_attempted()) {
    global $install_state;
    return $install_state['profile_info']['distribution_name'];
  }
  // At all other times, we load the profile via standard methods.
  else {
    $profile = drupal_get_profile();
    $info = system_get_info('module', $profile);
    return $info['distribution_name'];
  }
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
