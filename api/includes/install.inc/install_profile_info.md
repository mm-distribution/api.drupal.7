# install_profile_info()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 1294–1321 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L1294-L1321)

## Signature

```php
function install_profile_info($profile, $locale = 'en')
```

## Documentation

```text
Retrieves information about an installation profile from its .info file.

The information stored in a profile .info file is similar to that stored in
a normal Drupal module .info file. For example:
- name: The real name of the installation profile for display purposes.
- description: A brief description of the profile.
- dependencies: An array of shortnames of other modules that this install
  profile requires.

Additional, less commonly-used information that can appear in a profile.info
file but not in a normal Drupal module .info file includes:
- distribution_name: The name of the Drupal distribution that is being
  installed, to be shown throughout the installation process. Defaults to
  'Drupal'.
- exclusive: If the install profile is intended to be the only eligible
  choice in a distribution, setting exclusive = TRUE will auto-select it
  during installation, and the install profile selection screen will be
  skipped. If more than one profile is found where exclusive = TRUE then
  this property will have no effect and the profile selection screen will
  be shown as normal with all available profiles shown.

Note that this function does an expensive file system scan to get info file
information for dependencies. If you only need information from the info
file itself, use system_get_info().

Example of .info file:
@code
   name = Minimal
   description = Start fresh, with only a few modules enabled.
   dependencies[] = block
   dependencies[] = dblog
@endcode

@param $profile
  Name of profile.
@param $locale
  Name of locale used (if any).

@return
  The info array.
```

## Code

```php
function install_profile_info($profile, $locale = 'en') {
  $cache = &drupal_static(__FUNCTION__, array());

  if (!isset($cache[$profile])) {
    // Set defaults for module info.
    $defaults = array(
      'dependencies' => array(),
      'description' => '',
      'distribution_name' => 'Drupal',
      'version' => NULL,
      'hidden' => FALSE,
      'php' => DRUPAL_MINIMUM_PHP,
    );
    $info = drupal_parse_info_file("profiles/$profile/$profile.info") + $defaults;
    $info['dependencies'] = array_unique(array_merge(
      drupal_required_modules(),
      $info['dependencies'],
      ($locale != 'en' && !empty($locale) ? array('locale') : array()))
    );

    // drupal_required_modules() includes the current profile as a dependency.
    // Since a module can't depend on itself we remove that element of the array.
    array_shift($info['dependencies']);

    $cache[$profile] = $info;
  }
  return $cache[$profile];
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
