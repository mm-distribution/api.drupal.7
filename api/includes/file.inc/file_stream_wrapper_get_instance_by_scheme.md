# file_stream_wrapper_get_instance_by_scheme()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 345–355 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L345-L355)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_stream_wrapper_get_instance_by_scheme($scheme)
```

## Documentation

```text
Returns a reference to the stream wrapper class responsible for a scheme.

This helper method returns a stream instance using a scheme. That is, the
passed string does not contain a "://". For example, "public" is a scheme
but "public://" is a URI (stream). This is because the later contains both
a scheme and target despite target being empty.

Note: the instance URI will be initialized to "scheme://" so that you can
make the customary method calls as if you had retrieved an instance by URI.

@param $scheme
  If the stream was "public://target", "public" would be the scheme.

@return
  Returns a new stream wrapper object appropriate for the given $scheme.
  For example, for the public scheme a stream wrapper object
  (DrupalPublicStreamWrapper).
  FALSE is returned if no registered handler could be found.
```

## Code

```php
function file_stream_wrapper_get_instance_by_scheme($scheme) {
  $class = file_stream_wrapper_get_class($scheme);
  if (class_exists($class)) {
    $instance = new $class();
    $instance->setUri($scheme . '://');
    return $instance;
  }
  else {
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
