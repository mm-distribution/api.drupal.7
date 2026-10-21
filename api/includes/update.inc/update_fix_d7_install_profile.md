# update_fix_d7_install_profile()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 795–855 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L795-L855)

## Signature

```php
function update_fix_d7_install_profile()
```

## Documentation

```text
Register the currently installed profile in the system table.

Installation profiles are now treated as modules by Drupal, and have an
upgrade path based on their schema version in the system table.

The installation profile will be set to schema_version 0, as it has already
been installed. Any other hook_update_N functions provided by the
installation profile will be run by update.php.
```

## Code

```php
function update_fix_d7_install_profile() {
  $profile = drupal_get_profile();

  // 'Default' profile has been renamed to 'Standard' in D7.
  // We change the profile here to prevent a broken record in the system table.
  // See system_update_7049().
  if ($profile == 'default') {
    $profile = 'standard';
    variable_set('install_profile', $profile);
  }

  $results = db_select('system', 's')
    ->fields('s', array('name', 'schema_version'))
    ->condition('name', $profile)
    ->condition('type', 'module')
    ->execute()
    ->fetchAll();

  if (empty($results)) {
    $filename = 'profiles/' . $profile . '/' . $profile . '.profile';

    // Read profile info file
    $info = drupal_parse_info_file(dirname($filename) . '/' . $profile . '.info');

    // Merge in defaults.
    $info = $info + array(
      'dependencies' => array(),
      'description' => '',
      'package' => 'Other',
      'version' => NULL,
      'php' => DRUPAL_MINIMUM_PHP,
      'files' => array(),
    );

    $values = array(
      'filename' => $filename,
      'name' => $profile,
      'info' => serialize($info),
      'schema_version' => 0,
      'type' => 'module',
      'status' => 1,
      'owner' => '',
    );

    // Installation profile hooks are always executed last by the module system
    $values['weight'] = 1000;

    // Initializing the system table entry for the installation profile
    db_insert('system')
      ->fields(array_keys($values))
      ->values($values)
      ->execute();

    // Reset the cached schema version.
    drupal_get_installed_schema_version($profile, TRUE);

    // Load the updates again to make sure the installation profile updates
    // are loaded.
    drupal_load_updates();
  }
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
