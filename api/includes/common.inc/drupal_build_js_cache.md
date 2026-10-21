# drupal_build_js_cache()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5214–5263 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5214-L5263)

## Signature

```php
function drupal_build_js_cache($files)
```

## Documentation

```text
Aggregates JavaScript files into a cache file in the files directory.

The file name for the JavaScript cache file is generated from the hash of
the aggregated contents of the files in $files. This forces proxies and
browsers to download new JavaScript when the JavaScript changes.

The cache file name is retrieved on a page load via a lookup variable that
contains an associative array. The array key is the hash of the names in
$files while the value is the cache file name. The cache file is generated
in two cases. First, if there is no file name value for the key, which will
happen if a new file name has been added to $files or after the lookup
variable is emptied to force a rebuild of the cache. Second, the cache file
is generated if it is missing on disk. Old cache files are not deleted
immediately when the lookup variable is emptied, but are deleted after a set
period by drupal_delete_file_if_stale(). This ensures that files referenced
by a cached page will still be available.

@param $files
  An array of JavaScript files to aggregate and compress into one file.

@return
  The URI of the cache file, or FALSE if the file could not be saved.
```

## Code

```php
function drupal_build_js_cache($files) {
  $contents = '';
  $uri = '';
  $map = variable_get('drupal_js_cache_files', array());
  // Create a new array so that only the file names are used to create the hash.
  // This prevents new aggregates from being created unnecessarily.
  $js_data = array();
  foreach ($files as $file) {
    $js_data[] = $file['data'];
  }
  $key = hash('sha256', serialize($js_data));
  if (isset($map[$key])) {
    $uri = $map[$key];
  }

  if (empty($uri) || !file_exists($uri)) {
    // Build aggregate JS file.
    foreach ($files as $path => $info) {
      if ($info['preprocess']) {
        // Append a ';' and a newline after each JS file to prevent them from running together.
        $contents .= file_get_contents($path) . ";\n";
      }
    }
    // Remove JS source and source mapping urls or these may cause 404 errors.
    $contents = preg_replace('/\/\/(#|@)\s(sourceURL|sourceMappingURL)=\s*(\S*?)\s*$/m', '', $contents);
    // Prefix filename to prevent blocking by firewalls which reject files
    // starting with "ad*".
    $filename = 'js_' . drupal_hash_base64($contents) . '.js';
    // Create the js/ within the files folder.
    $jspath = 'public://js';
    $uri = $jspath . '/' . $filename;
    // Create the JS file.
    file_prepare_directory($jspath, FILE_CREATE_DIRECTORY);
    if (!file_exists($uri) && !file_unmanaged_save_data($contents, $uri, FILE_EXISTS_REPLACE)) {
      return FALSE;
    }
    // If JS gzip compression is enabled, clean URLs are enabled (which means
    // that rewrite rules are working) and the zlib extension is available then
    // create a gzipped version of this file. This file is served conditionally
    // to browsers that accept gzip using .htaccess rules.
    if (variable_get('js_gzip_compression', TRUE) && variable_get('clean_url', 0) && extension_loaded('zlib')) {
      if (!file_exists($uri . '.gz') && !file_unmanaged_save_data(gzencode($contents, 9, FORCE_GZIP), $uri . '.gz', FILE_EXISTS_REPLACE)) {
        return FALSE;
      }
    }
    $map[$key] = $uri;
    variable_set('drupal_js_cache_files', $map);
  }
  return $uri;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
