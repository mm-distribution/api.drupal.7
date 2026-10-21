# update_manager_file_get()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 831–849 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L831-L849)
- **Module/theme:** update
- **Topics:** [update_manager_file](../../../topics/update_manager_file.md)

## Signature

```php
function update_manager_file_get($url)
```

## Documentation

```text
Copies a file from the specified URL to the temporary directory for updates.

Returns the local path if the file has already been downloaded.

@param $url
  The URL of the file on the server.

@return string
  Path to local file.
```

## Code

```php
function update_manager_file_get($url) {
  $parsed_url = parse_url($url);
  $remote_schemes = array('http', 'https', 'ftp', 'ftps', 'smb', 'nfs');
  if (!in_array($parsed_url['scheme'], $remote_schemes)) {
    // This is a local file, just return the path.
    return drupal_realpath($url);
  }

  // Check the cache and download the file if needed.
  $cache_directory = _update_manager_cache_directory();
  $local = $cache_directory . '/' . drupal_basename($parsed_url['path']);

  if (!file_exists($local) || update_delete_file_if_stale($local)) {
    return system_retrieve_file($url, $local, FALSE, FILE_EXISTS_REPLACE);
  }
  else {
    return $local;
  }
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
