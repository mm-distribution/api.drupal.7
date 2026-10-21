# update_verify_update_archive()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 683–734 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L683-L734)
- **Module/theme:** update
- **Implements:** [hook_verify_update_archive()](../update.api.php/hook_verify_update_archive.md)

## Signature

```php
function update_verify_update_archive($project, $archive_file, $directory)
```

## Documentation

```text
Implements hook_verify_update_archive().

First, we ensure that the archive isn't a copy of Drupal core, which the
update manager does not yet support. See http://drupal.org/node/606592

Then, we make sure that at least one module included in the archive file has
an .info file which claims that the code is compatible with the current
version of Drupal core.

@see drupal_system_listing()
@see _system_rebuild_module_data()
```

## Code

```php
function update_verify_update_archive($project, $archive_file, $directory) {
  $errors = array();

  // Make sure this isn't a tarball of Drupal core.
  if (
    file_exists("$directory/$project/index.php")
    && file_exists("$directory/$project/update.php")
    && file_exists("$directory/$project/includes/bootstrap.inc")
    && file_exists("$directory/$project/modules/node/node.module")
    && file_exists("$directory/$project/modules/system/system.module")
  ) {
    return array(
      'no-core' => t('Automatic updating of Drupal core is not supported. See the <a href="@upgrade-guide">upgrade guide</a> for information on how to update Drupal core manually.', array('@upgrade-guide' => 'http://drupal.org/upgrade')),
    );
  }

  // Parse all the .info files and make sure at least one is compatible with
  // this version of Drupal core. If one is compatible, then the project as a
  // whole is considered compatible (since, for example, the project may ship
  // with some out-of-date modules that are not necessary for its overall
  // functionality).
  $compatible_project = FALSE;
  $incompatible = array();
  $files = file_scan_directory("$directory/$project", '/^' . DRUPAL_PHP_FUNCTION_PATTERN . '\.info$/', array('key' => 'name', 'min_depth' => 0));
  foreach ($files as $key => $file) {
    // Get the .info file for the module or theme this file belongs to.
    $info = drupal_parse_info_file($file->uri);

    // If the module or theme is incompatible with Drupal core, set an error.
    if (empty($info['core']) || $info['core'] != DRUPAL_CORE_COMPATIBILITY) {
      $incompatible[] = !empty($info['name']) ? $info['name'] : t('Unknown');
    }
    else {
      $compatible_project = TRUE;
      break;
    }
  }

  if (empty($files)) {
    $errors[] = t('%archive_file does not contain any .info files.', array('%archive_file' => drupal_basename($archive_file)));
  }
  elseif (!$compatible_project) {
    $errors[] = format_plural(
      count($incompatible),
      '%archive_file contains a version of %names that is not compatible with Drupal !version.',
      '%archive_file contains versions of modules or themes that are not compatible with Drupal !version: %names',
      array('!version' => DRUPAL_CORE_COMPATIBILITY, '%archive_file' => drupal_basename($archive_file), '%names' => implode(', ', $incompatible))
    );
  }

  return $errors;
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
