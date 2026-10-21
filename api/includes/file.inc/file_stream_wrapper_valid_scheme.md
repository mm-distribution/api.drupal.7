# file_stream_wrapper_valid_scheme()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 225–234 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L225-L234)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_stream_wrapper_valid_scheme($scheme)
```

## Documentation

```text
Checks that the scheme of a stream URI is valid.

Confirms that there is a registered stream handler for the provided scheme
and that it is callable. This is useful if you want to confirm a valid
scheme without creating a new instance of the registered handler.

@param $scheme
  A URI scheme, a stream is referenced as "scheme://target".

@return
  Returns TRUE if the string is the name of a validated stream,
  or FALSE if the scheme does not have a registered handler.
```

## Code

```php
function file_stream_wrapper_valid_scheme($scheme) {
  // Does the scheme have a registered handler that is callable?
  $class = file_stream_wrapper_get_class($scheme);
  if (class_exists($class)) {
    return TRUE;
  }
  else {
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
