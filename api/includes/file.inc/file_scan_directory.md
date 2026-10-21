# file_scan_directory()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2195–2260 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2195-L2260)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_scan_directory($dir, $mask, $options = array(), $depth = 0)
```

## Documentation

```text
Finds all files that match a given mask in a given directory.

Directories and files beginning with a period are excluded; this
prevents hidden files and directories (such as SVN working directories)
from being scanned.

@param $dir
  The base directory or URI to scan, without trailing slash.
@param $mask
  The preg_match() regular expression of the files to find.
@param $options
  An associative array of additional options, with the following elements:
  - 'nomask': The preg_match() regular expression of the files to ignore.
    Defaults to '/(\.\.?|CVS)$/'.
  - 'callback': The callback function to call for each match. There is no
    default callback.
  - 'recurse': When TRUE, the directory scan will recurse the entire tree
    starting at the provided directory. Defaults to TRUE.
  - 'key': The key to be used for the returned associative array of files.
    Possible values are 'uri', for the file's URI; 'filename', for the
    basename of the file; and 'name' for the name of the file without the
    extension. Defaults to 'uri'.
  - 'min_depth': Minimum depth of directories to return files from. Defaults
    to 0.
@param $depth
  Current depth of recursion. This parameter is only used internally and
  should not be passed in.

@return
  An associative array (keyed on the chosen key) of objects with 'uri',
  'filename', and 'name' members corresponding to the matching files.
```

## Code

```php
function file_scan_directory($dir, $mask, $options = array(), $depth = 0) {
  // Default nomask option.
  $nomask = '/(\.\.?|CVS)$/';

  // Overrides the $nomask variable accordingly if $options['nomask'] is set.
  //
  // Allow directories specified in settings.php to be ignored. You can use this
  // to not check for files in common special-purpose directories. For example,
  // node_modules and bower_components. Ignoring irrelevant directories is a
  // performance boost.
  if (!isset($options['nomask'])) {
    $ignore_directories = variable_get(
      'file_scan_ignore_directories',
      array()
    );

    foreach ($ignore_directories as $index => $ignore_directory) {
      $ignore_directories[$index] = preg_quote($ignore_directory, '/');
    }

    if (!empty($ignore_directories)) {
      $nomask = '/^(\.\.?)|CVS|' . implode('|', $ignore_directories) . '$/';
    }
  }

  // Merge in defaults.
  $options += array(
    'nomask' => $nomask,
    'callback' => 0,
    'recurse' => TRUE,
    'key' => 'uri',
    'min_depth' => 0,
  );

  $options['key'] = in_array($options['key'], array('uri', 'filename', 'name')) ? $options['key'] : 'uri';
  $files = array();
  if (is_dir($dir) && $handle = opendir($dir)) {
    while (FALSE !== ($filename = readdir($handle))) {
      if (!preg_match($options['nomask'], $filename) && $filename[0] != '.') {
        $uri = "$dir/$filename";
        $uri = file_stream_wrapper_uri_normalize($uri);
        if (is_dir($uri) && $options['recurse']) {
          // Give priority to files in this folder by merging them in after any subdirectory files.
          $files = array_merge(file_scan_directory($uri, $mask, $options, $depth + 1), $files);
        }
        elseif ($depth >= $options['min_depth'] && preg_match($mask, $filename)) {
          // Always use this match over anything already set in $files with the
          // same $$options['key'].
          $file = new stdClass();
          $file->uri = $uri;
          $file->filename = $filename;
          $file->name = pathinfo($filename, PATHINFO_FILENAME);
          $key = $options['key'];
          $files[$file->$key] = $file;
          if ($options['callback']) {
            $options['callback']($uri);
          }
        }
      }
    }

    closedir($handle);
  }

  return $files;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
