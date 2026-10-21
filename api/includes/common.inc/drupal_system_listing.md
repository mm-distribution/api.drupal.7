# drupal_system_listing()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5700–5770 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5700-L5770)

## Signature

```php
function drupal_system_listing($mask, $directory, $key = 'name', $min_depth = 1)
```

## Documentation

```text
Returns information about system object files (modules, themes, etc.).

This function is used to find all or some system object files (module files,
theme files, etc.) that exist on the site. It searches in several locations,
depending on what type of object you are looking for. For instance, if you
are looking for modules and call:
@code
drupal_system_listing("/\.module$/", "modules", 'name', 0);
@endcode
this function will search the site-wide modules directory (i.e., /modules/),
your installation profile's directory (i.e.,
/profiles/your_site_profile/modules/), the all-sites directory (i.e.,
/sites/all/modules/), and your site-specific directory (i.e.,
/sites/your_site_dir/modules/), in that order, and return information about
all of the files ending in .module in those directories.

The information is returned in an associative array, which can be keyed on
the file name ($key = 'filename'), the file name without the extension ($key
= 'name'), or the full file stream URI ($key = 'uri'). If you use a key of
'filename' or 'name', files found later in the search will take precedence
over files found earlier (unless they belong to a module or theme not
compatible with Drupal core); if you choose a key of 'uri', you will get all
files found.

@param string $mask
  The preg_match() regular expression for the files to find.
@param string $directory
  The subdirectory name in which the files are found. For example,
  'modules' will search in sub-directories of the top-level /modules
  directory, sub-directories of /sites/all/modules/, etc.
@param string $key
  The key to be used for the associative array returned. Possible values are
  'uri', for the file's URI; 'filename', for the basename of the file; and
  'name' for the name of the file without the extension. If you choose 'name'
  or 'filename', only the highest-precedence file will be returned.
@param int $min_depth
  Minimum depth of directories to return files from, relative to each
  directory searched. For instance, a minimum depth of 2 would find modules
  inside /modules/node/tests, but not modules directly in /modules/node.

@return array
  An associative array of file objects, keyed on the chosen key. Each element
  in the array is an object containing file information, with properties:
  - 'uri': Full URI of the file.
  - 'filename': File name.
  - 'name': Name of file without the extension.
```

## Code

```php
function drupal_system_listing($mask, $directory, $key = 'name', $min_depth = 1) {
  $config = conf_path();

  $searchdir = array($directory);
  $files = array();

  // The 'profiles' directory contains pristine collections of modules and
  // themes as organized by a distribution. It is pristine in the same way
  // that /modules is pristine for core; users should avoid changing anything
  // there in favor of sites/all or sites/<domain> directories.
  $profiles = array();
  $profile = drupal_get_profile();
  // For SimpleTest to be able to test modules packaged together with a
  // distribution we need to include the profile of the parent site (in which
  // test runs are triggered).
  if (drupal_valid_test_ua()) {
    $testing_profile = variable_get('simpletest_parent_profile', FALSE);
    if ($testing_profile && $testing_profile != $profile) {
      $profiles[] = $testing_profile;
    }
  }
  // In case both profile directories contain the same extension, the actual
  // profile always has precedence.
  $profiles[] = $profile;
  foreach ($profiles as $profile) {
    if (file_exists("profiles/$profile/$directory")) {
      $searchdir[] = "profiles/$profile/$directory";
    }
  }

  // Always search sites/all/* as well as the global directories.
  $searchdir[] = 'sites/all/' . $directory;

  if (file_exists("$config/$directory")) {
    $searchdir[] = "$config/$directory";
  }

  // Get current list of items.
  if (!function_exists('file_scan_directory')) {
    require_once DRUPAL_ROOT . '/includes/file.inc';
  }
  foreach ($searchdir as $dir) {
    $files_to_add = file_scan_directory($dir, $mask, array('key' => $key, 'min_depth' => $min_depth));

    // Duplicate files found in later search directories take precedence over
    // earlier ones, so we want them to overwrite keys in our resulting
    // $files array.
    // The exception to this is if the later file is from a module or theme not
    // compatible with Drupal core. This may occur during upgrades of Drupal
    // core when new modules exist in core while older contrib modules with the
    // same name exist in a directory such as sites/all/modules/.
    foreach (array_intersect_key($files_to_add, $files) as $file_key => $file) {
      // If it has no info file, then we just behave liberally and accept the
      // new resource on the list for merging.
      if (file_exists($info_file = dirname($file->uri) . '/' . $file->name . '.info')) {
        // Get the .info file for the module or theme this file belongs to.
        $info = drupal_parse_info_file($info_file);

        // If the module or theme is incompatible with Drupal core, remove it
        // from the array for the current search directory, so it is not
        // overwritten when merged with the $files array.
        if (isset($info['core']) && $info['core'] != DRUPAL_CORE_COMPATIBILITY) {
          unset($files_to_add[$file_key]);
        }
      }
    }
    $files = array_merge($files, $files_to_add);
  }

  return $files;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
