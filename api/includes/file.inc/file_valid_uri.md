# file_valid_uri()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 872–879 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L872-L879)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_valid_uri($uri)
```

## Documentation

```text
Determines whether the URI has a valid scheme for file API operations.

There must be a scheme and it must be a Drupal-provided scheme like
'public', 'private', 'temporary', or an extension provided with
hook_stream_wrappers().

@param $uri
  The URI to be tested.

@return
  TRUE if the URI is allowed.
```

## Code

```php
function file_valid_uri($uri) {
  // Assert that the URI has an allowed scheme. Barepaths are not allowed.
  $uri_scheme = file_uri_scheme($uri);
  if (empty($uri_scheme) || !file_stream_wrapper_valid_scheme($uri_scheme)) {
    return FALSE;
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
