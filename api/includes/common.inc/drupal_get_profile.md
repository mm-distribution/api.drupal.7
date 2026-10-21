# drupal_get_profile()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 222–233 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L222-L233)

## Signature

```php
function drupal_get_profile()
```

## Documentation

```text
Gets the name of the currently active installation profile.

When this function is called during Drupal's initial installation process,
the name of the profile that's about to be installed is stored in the global
installation state. At all other times, the standard Drupal systems variable
table contains the name of the current profile, and we can call
variable_get() to determine what one is active.

@return $profile
  The name of the installation profile.
```

## Code

```php
function drupal_get_profile() {
  global $install_state;

  if (isset($install_state['parameters']['profile'])) {
    $profile = $install_state['parameters']['profile'];
  }
  else {
    $profile = variable_get('install_profile', 'standard');
  }

  return $profile;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
