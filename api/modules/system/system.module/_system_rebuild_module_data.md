# _system_rebuild_module_data()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2392–2475 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2392-L2475)
- **Module/theme:** system

## Signature

```php
function _system_rebuild_module_data()
```

## Documentation

```text
Helper function to scan and collect module .info data.

@return
  An associative array of module information.
```

## Code

```php
function _system_rebuild_module_data() {
  // Find modules
  $modules = drupal_system_listing('/^' . DRUPAL_PHP_FUNCTION_PATTERN . '\.module$/', 'modules', 'name', 0);

  // Include the installation profile in modules that are loaded.
  $profile = drupal_get_profile();
  $modules[$profile] = new stdClass();
  $modules[$profile]->name = $profile;
  $modules[$profile]->uri = 'profiles/' . $profile . '/' . $profile . '.profile';
  $modules[$profile]->filename = $profile . '.profile';

  // Installation profile hooks are always executed last.
  $modules[$profile]->weight = 1000;

  // Set defaults for module info.
  $defaults = array(
    'dependencies' => array(),
    'description' => '',
    'package' => 'Other',
    'version' => NULL,
    'php' => DRUPAL_MINIMUM_PHP,
    'files' => array(),
    'bootstrap' => 0,
  );

  // Read info files for each module.
  foreach ($modules as $key => $module) {
    // The module system uses the key 'filename' instead of 'uri' so copy the
    // value so it will be used by the modules system.
    $modules[$key]->filename = $module->uri;

    // Look for the info file.
    $module->info = drupal_parse_info_file(dirname($module->uri) . '/' . $module->name . '.info');

    // Skip modules that don't provide info.
    if (empty($module->info)) {
      unset($modules[$key]);
      continue;
    }

    // Add the info file modification time, so it becomes available for
    // contributed modules to use for ordering module lists.
    $module->info['mtime'] = filemtime(dirname($module->uri) . '/' . $module->name . '.info');

    // Merge in defaults and save.
    $modules[$key]->info = $module->info + $defaults;

    // The "name" key is required, but to avoid a fatal error in the menu system
    // we set a reasonable default if it is not provided.
    $modules[$key]->info += array('name' => $key);

    // Prefix stylesheets and scripts with module path.
    $path = dirname($module->uri);
    if (isset($module->info['stylesheets'])) {
      $module->info['stylesheets'] = _system_info_add_path($module->info['stylesheets'], $path);
    }
    if (isset($module->info['scripts'])) {
      $module->info['scripts'] = _system_info_add_path($module->info['scripts'], $path);
    }

    // Installation profiles are hidden by default, unless explicitly specified
    // otherwise in the .info file.
    if ($key == $profile && !isset($modules[$key]->info['hidden'])) {
      $modules[$key]->info['hidden'] = TRUE;
    }

    // Invoke hook_system_info_alter() to give installed modules a chance to
    // modify the data in the .info files if necessary.
    $type = 'module';
    drupal_alter('system_info', $modules[$key]->info, $modules[$key], $type);
  }

  if (isset($modules[$profile])) {
    // The installation profile is required, if it's a valid module.
    $modules[$profile]->info['required'] = TRUE;
    // Add a default distribution name if the profile did not provide one. This
    // matches the default value used in install_profile_info().
    if (!isset($modules[$profile]->info['distribution_name'])) {
      $modules[$profile]->info['distribution_name'] = 'Drupal';
    }
  }

  return $modules;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
