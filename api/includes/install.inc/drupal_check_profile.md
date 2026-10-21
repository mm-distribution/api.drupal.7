# drupal_check_profile()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 1178–1199 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L1178-L1199)

## Signature

```php
function drupal_check_profile($profile)
```

## Documentation

```text
Checks an installation profile's requirements.

@param $profile
  Name of installation profile to check.
@return
  Array of the installation profile's requirements.
```

## Code

```php
function drupal_check_profile($profile) {
  include_once DRUPAL_ROOT . '/includes/file.inc';

  $profile_file = DRUPAL_ROOT . "/profiles/$profile/$profile.profile";

  if (!isset($profile) || !file_exists($profile_file)) {
    throw new Exception(install_no_profile_error());
  }

  $info = install_profile_info($profile);

  // Collect requirement testing results.
  $requirements = array();
  foreach ($info['dependencies'] as $module) {
    module_load_install($module);
    $function = $module . '_requirements';
    if (function_exists($function)) {
      $requirements = array_merge($requirements, $function('install'));
    }
  }
  return $requirements;
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
