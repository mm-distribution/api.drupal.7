# file_stream_wrapper_get_instance_by_uri()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 312–323 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L312-L323)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_stream_wrapper_get_instance_by_uri($uri)
```

## Documentation

```text
Returns a reference to the stream wrapper class responsible for a given URI.

The scheme determines the stream wrapper class that should be
used by consulting the stream wrapper registry.

@param $uri
  A stream, referenced as "scheme://target".

@return
  Returns a new stream wrapper object appropriate for the given URI or FALSE
  if no registered handler could be found. For example, a URI of
  "private://example.txt" would return a new private stream wrapper object
  (DrupalPrivateStreamWrapper).
```

## Code

```php
function file_stream_wrapper_get_instance_by_uri($uri) {
  $scheme = file_uri_scheme($uri);
  $class = file_stream_wrapper_get_class($scheme);
  if (class_exists($class)) {
    $instance = new $class();
    $instance->setUri($uri);
    return $instance;
  }
  else {
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
