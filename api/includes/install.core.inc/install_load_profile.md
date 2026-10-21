# install_load_profile()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1377–1386 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1377-L1386)

## Signature

```php
function install_load_profile(&$install_state)
```

## Documentation

```text
Loads information about the chosen profile during installation.

@param $install_state
  An array of information about the current installation state. The loaded
  profile information will be added here, or an exception will be thrown if
  the profile cannot be loaded.
```

## Code

```php
function install_load_profile(&$install_state) {
  $profile_file = DRUPAL_ROOT . '/profiles/' . $install_state['parameters']['profile'] . '/' . $install_state['parameters']['profile'] . '.profile';
  if (file_exists($profile_file)) {
    include_once $profile_file;
    $install_state['profile_info'] = install_profile_info($install_state['parameters']['profile'], $install_state['parameters']['locale']);
  }
  else {
    throw new Exception(st('Sorry, the profile you have chosen cannot be loaded.'));
  }
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
