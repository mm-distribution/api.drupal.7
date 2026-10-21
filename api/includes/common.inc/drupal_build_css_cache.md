# drupal_build_css_cache()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3728–3798 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3728-L3798)

## Signature

```php
function drupal_build_css_cache($css)
```

## Documentation

```text
Aggregates and optimizes CSS files into a cache file in the files directory.

The file name for the CSS cache file is generated from the hash of the
aggregated contents of the files in $css. This forces proxies and browsers
to download new CSS when the CSS changes.

The cache file name is retrieved on a page load via a lookup variable that
contains an associative array. The array key is the hash of the file names
in $css while the value is the cache file name. The cache file is generated
in two cases. First, if there is no file name value for the key, which will
happen if a new file name has been added to $css or after the lookup
variable is emptied to force a rebuild of the cache. Second, the cache file
is generated if it is missing on disk. Old cache files are not deleted
immediately when the lookup variable is emptied, but are deleted after a set
period by drupal_delete_file_if_stale(). This ensures that files referenced
by a cached page will still be available.

@param $css
  An array of CSS files to aggregate and compress into one file.

@return
  The URI of the CSS cache file, or FALSE if the file could not be saved.
```

## Code

```php
function drupal_build_css_cache($css) {
  $data = '';
  $uri = '';
  $map = variable_get('drupal_css_cache_files', array());
  // Create a new array so that only the file names are used to create the hash.
  // This prevents new aggregates from being created unnecessarily.
  $css_data = array();
  foreach ($css as $css_file) {
    $css_data[] = $css_file['data'];
  }
  $key = hash('sha256', serialize($css_data));
  if (isset($map[$key])) {
    $uri = $map[$key];
  }

  if (empty($uri) || !file_exists($uri)) {
    // Build aggregate CSS file.
    foreach ($css as $stylesheet) {
      // Only 'file' stylesheets can be aggregated.
      if ($stylesheet['type'] == 'file') {
        $contents = drupal_load_stylesheet($stylesheet['data'], TRUE);

        // Build the base URL of this CSS file: start with the full URL.
        $css_base_url = file_create_url($stylesheet['data']);
        // Move to the parent.
        $css_base_url = substr($css_base_url, 0, strrpos($css_base_url, '/'));
        // Simplify to a relative URL if the stylesheet URL starts with the
        // base URL of the website.
        if (substr($css_base_url, 0, strlen($GLOBALS['base_root'])) == $GLOBALS['base_root']) {
          $css_base_url = substr($css_base_url, strlen($GLOBALS['base_root']));
        }

        _drupal_build_css_path(NULL, $css_base_url . '/');
        // Anchor all paths in the CSS with its base URL, ignoring external and absolute paths.
        $data .= preg_replace_callback('/url\(\s*[\'"]?(?![a-z]+:|\/+)([^\'")]+)[\'"]?\s*\)/i', '_drupal_build_css_path', $contents);
      }
    }

    // Per the W3C specification at http://www.w3.org/TR/REC-CSS2/cascade.html#at-import,
    // @import rules must proceed any other style, so we move those to the top.
    $regexp = '/@import[^;]+;/i';
    preg_match_all($regexp, $data, $matches);
    $data = preg_replace($regexp, '', $data);
    $data = implode('', $matches[0]) . $data;

    // Prefix filename to prevent blocking by firewalls which reject files
    // starting with "ad*".
    $filename = 'css_' . drupal_hash_base64($data) . '.css';
    // Create the css/ within the files folder.
    $csspath = 'public://css';
    $uri = $csspath . '/' . $filename;
    // Create the CSS file.
    file_prepare_directory($csspath, FILE_CREATE_DIRECTORY);
    if (!file_exists($uri) && !file_unmanaged_save_data($data, $uri, FILE_EXISTS_REPLACE)) {
      return FALSE;
    }
    // If CSS gzip compression is enabled, clean URLs are enabled (which means
    // that rewrite rules are working) and the zlib extension is available then
    // create a gzipped version of this file. This file is served conditionally
    // to browsers that accept gzip using .htaccess rules.
    if (variable_get('css_gzip_compression', TRUE) && variable_get('clean_url', 0) && extension_loaded('zlib')) {
      if (!file_exists($uri . '.gz') && !file_unmanaged_save_data(gzencode($data, 9, FORCE_GZIP), $uri . '.gz', FILE_EXISTS_REPLACE)) {
        return FALSE;
      }
    }
    // Save the updated map.
    $map[$key] = $uri;
    variable_set('drupal_css_cache_files', $map);
  }
  return $uri;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
