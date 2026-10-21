# file_download_access()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2158–2160 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2158-L2160)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_download_access($uri)
```

## Documentation

```text
Checks that the current user has access to a particular file.

The return value of this function hinges on the return value from
file_download_headers(), which is the function responsible for collecting
access information through hook_file_download().

If immediately transferring the file to the browser and the headers will
need to be retrieved, the return value of file_download_headers() should be
used to determine access directly, so that access checks will not be run
twice.

@param $uri
  The URI for the file whose access should be retrieved.

@return
  Boolean TRUE if access is allowed. FALSE if access is not allowed.

@see file_download_headers()
@see hook_file_download()
```

## Code

```php
function file_download_access($uri) {
  return count(file_download_headers($uri)) > 0;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
