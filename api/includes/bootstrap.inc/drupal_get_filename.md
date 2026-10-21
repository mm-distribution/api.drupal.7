# drupal_get_filename()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 895–954 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L895-L954)

## Signature

```php
function drupal_get_filename($type, $name, $filename = NULL, $trigger_error = TRUE)
```

## Documentation

```text
Returns and optionally sets the filename for a system resource.

The filename, whether provided, cached, or retrieved from the database, is
only returned if the file exists.

This function plays a key role in allowing Drupal's resources (modules
and themes) to be located in different places depending on a site's
configuration. For example, a module 'foo' may legally be located
in any of these three places:

modules/foo/foo.module
sites/all/modules/foo/foo.module
sites/example.com/modules/foo/foo.module

Calling drupal_get_filename('module', 'foo') will give you one of
the above, depending on where the module is located.

@param $type
  The type of the item (theme, theme_engine, module, profile).
@param $name
  The name of the item for which the filename is requested.
@param $filename
  The filename of the item if it is to be set explicitly rather
  than by consulting the database.
@param bool $trigger_error
  Whether to trigger an error when a file is missing or has unexpectedly
  moved. This defaults to TRUE, but can be set to FALSE by calling code that
  merely wants to check whether an item exists in the filesystem.

@return
  The filename of the requested item or NULL if the item is not found.
```

## Code

```php
function drupal_get_filename($type, $name, $filename = NULL, $trigger_error = TRUE) {
  // The $files static variable will hold the locations of all requested files.
  // We can be sure that any file listed in this static variable actually
  // exists as all additions have gone through a file_exists() check.
  // The location of files will not change during the request, so do not use
  // drupal_static().
  static $files = array();

  // Profiles are a special case: they have a fixed location and naming.
  if ($type == 'profile') {
    $profile_filename = "profiles/$name/$name.profile";
    $files[$type][$name] = file_exists($profile_filename) ? $profile_filename : FALSE;
  }
  if (!isset($files[$type])) {
    $files[$type] = array();
  }

  if (!empty($filename) && file_exists($filename)) {
    // Prime the static cache with the provided filename.
    $files[$type][$name] = $filename;
  }
  elseif (isset($files[$type][$name])) {
    // This item had already been found earlier in the request, either through
    // priming of the static cache (for example, in system_list()), through a
    // lookup in the {system} table, or through a file scan (cached or not). Do
    // nothing.
  }
  else {
    // Look for the filename listed in the {system} table. Verify that we have
    // an active database connection before doing so, since this function is
    // called both before we have a database connection (i.e. during
    // installation) and when a database connection fails.
    $database_unavailable = TRUE;
    try {
      if (function_exists('db_query')) {
        $file = db_query("SELECT filename FROM {system} WHERE name = :name AND type = :type", array(':name' => $name, ':type' => $type))->fetchField();
        if ($file !== FALSE && file_exists(DRUPAL_ROOT . '/' . $file)) {
          $files[$type][$name] = $file;
        }
        $database_unavailable = FALSE;
      }
    }
    catch (Exception $e) {
      // The database table may not exist because Drupal is not yet installed,
      // the database might be down, or we may have done a non-database cache
      // flush while $conf['page_cache_without_database'] = TRUE and
      // $conf['page_cache_invoke_hooks'] = TRUE. We have a fallback for these
      // cases so we hide the error completely.
    }
    // Fall back to searching the filesystem if the database could not find the
    // file or the file does not exist at the path returned by the database.
    if (!isset($files[$type][$name])) {
      $files[$type][$name] = _drupal_get_filename_fallback($type, $name, $trigger_error, $database_unavailable);
    }
  }

  if (isset($files[$type][$name])) {
    return $files[$type][$name];
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
