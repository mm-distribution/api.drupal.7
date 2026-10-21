# drupal_verify_profile()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 678–720 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L678-L720)

## Signature

```php
function drupal_verify_profile($install_state)
```

## Documentation

```text
Verifies an installation profile for installation.

@param $install_state
  An array of information about the current installation state.

@return
  The list of modules to install.
```

## Code

```php
function drupal_verify_profile($install_state) {
  $profile = $install_state['parameters']['profile'];
  $locale = $install_state['parameters']['locale'];

  include_once DRUPAL_ROOT . '/includes/file.inc';
  include_once DRUPAL_ROOT . '/includes/common.inc';

  $profile_file = DRUPAL_ROOT . "/profiles/$profile/$profile.profile";

  if (!isset($profile) || !file_exists($profile_file)) {
    throw new Exception(install_no_profile_error());
  }
  $info = $install_state['profile_info'];

  // Get a list of modules that exist in Drupal's assorted subdirectories.
  $present_modules = array();
  foreach (drupal_system_listing('/^' . DRUPAL_PHP_FUNCTION_PATTERN . '\.module$/', 'modules', 'name', 0) as $present_module) {
    $present_modules[] = $present_module->name;
  }

  // The installation profile is also a module, which needs to be installed
  // after all the other dependencies have been installed.
  $present_modules[] = drupal_get_profile();

  // Verify that all of the profile's required modules are present.
  $missing_modules = array_diff($info['dependencies'], $present_modules);

  $requirements = array();

  if (count($missing_modules)) {
    $modules = array();
    foreach ($missing_modules as $module) {
      $modules[] = '<span class="admin-missing">' . drupal_ucfirst($module) . '</span>';
    }
    $requirements['required_modules'] = array(
      'title'       => st('Required modules'),
      'value'       => st('Required modules not found.'),
      'severity'    => REQUIREMENT_ERROR,
      'description' => st('The following modules are required but were not found. Move them into the appropriate modules subdirectory, such as <em>sites/all/modules</em>. Missing modules: !modules', array('!modules' => implode(', ', $modules))),
    );
  }
  return $requirements;
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
