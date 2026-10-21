# file_download_headers()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2116–2135 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2116-L2135)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_download_headers($uri)
```

## Documentation

```text
Retrieves headers for a private file download.

Calls all module implementations of hook_file_download() to retrieve headers
for files by the module that originally provided the file. The presence of
returned headers indicates the current user has access to the file.

@param $uri
  The URI for the file whose headers should be retrieved.

@return
  If access is allowed, headers for the file, suitable for passing to
  file_transfer(). If access is not allowed, an empty array will be returned.

@see file_transfer()
@see file_download_access()
@see hook_file_download()
```

## Code

```php
function file_download_headers($uri) {
  // Let other modules provide headers and control access to the file.
  // module_invoke_all() uses array_merge_recursive() which merges header
  // values into a new array. To avoid that and allow modules to override
  // headers instead, use array_merge() to merge the returned arrays.
  $headers = array();
  foreach (module_implements('file_download') as $module) {
    $function = $module . '_file_download';
    $result = $function($uri);
    if ($result == -1) {
      // Throw away the headers received so far.
      $headers = array();
      break;
    }
    if (isset($result) && is_array($result)) {
      $headers = array_merge($headers, $result);
    }
  }
  return $headers;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
