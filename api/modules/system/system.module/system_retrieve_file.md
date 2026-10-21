# system_retrieve_file()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3534–3559 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3534-L3559)
- **Module/theme:** system

## Signature

```php
function system_retrieve_file($url, $destination = NULL, $managed = FALSE, $replace = FILE_EXISTS_RENAME)
```

## Documentation

```text
Attempts to get a file using drupal_http_request and to store it locally.

@param string $url
  The URL of the file to grab.
@param string $destination
  Stream wrapper URI specifying where the file should be placed. If a
  directory path is provided, the file is saved into that directory under
  its original name. If the path contains a filename as well, that one will
  be used instead.
  If this value is omitted, the site's default files scheme will be used,
  usually "public://".
@param bool $managed
  If this is set to TRUE, the file API hooks will be invoked and the file is
  registered in the database.
@param int $replace
  Replace behavior when the destination file already exists:
  - FILE_EXISTS_REPLACE: Replace the existing file.
  - FILE_EXISTS_RENAME: Append _{incrementing number} until the filename is
    unique.
  - FILE_EXISTS_ERROR: Do nothing and return FALSE.

@return mixed
  One of these possibilities:
  - If it succeeds and $managed is FALSE, the location where the file was
    saved.
  - If it succeeds and $managed is TRUE, a \Drupal\file\FileInterface
    object which describes the file.
  - If it fails, FALSE.
```

## Code

```php
function system_retrieve_file($url, $destination = NULL, $managed = FALSE, $replace = FILE_EXISTS_RENAME) {
  $parsed_url = parse_url($url);
  if (!isset($destination)) {
    $path = file_build_uri(drupal_basename($parsed_url['path']));
  }
  else {
    if (is_dir(drupal_realpath($destination))) {
      // Prevent URIs with triple slashes when glueing parts together.
      $path = str_replace('///', '//', "$destination/") . drupal_basename($parsed_url['path']);
    }
    else {
      $path = $destination;
    }
  }
  $result = drupal_http_request($url);
  if ($result->code != 200) {
    drupal_set_message(t('HTTP error @errorcode occurred when trying to fetch @remote.', array('@errorcode' => $result->code, '@remote' => $url)), 'error');
    return FALSE;
  }
  $local = $managed ? file_save_data($result->data, $path, $replace) : file_unmanaged_save_data($result->data, $path, $replace);
  if (!$local) {
    drupal_set_message(t('@remote could not be saved to @path.', array('@remote' => $url, '@path' => $path)), 'error');
  }

  return $local;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
