# file_uri_normalize_dot_segments()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2751–2792 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2751-L2792)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_uri_normalize_dot_segments($uri)
```

## Documentation

```text
Normalize dot segments in a URI.

@param $uri
  A stream, referenced as "scheme://target".

@return string
  The URI with dot segments removed and slashes as directory separator.
```

## Code

```php
function file_uri_normalize_dot_segments($uri) {
  $scheme = file_uri_scheme($uri);

  if (file_stream_wrapper_valid_scheme($scheme)) {
    $target = file_uri_target($uri);

    if ($target !== FALSE) {
      if (!in_array($scheme, variable_get('file_sa_core_2023_005_schemes', array()))) {
        $class = file_stream_wrapper_get_class($scheme);
        $is_local = is_subclass_of($class, 'DrupalLocalStreamWrapper');
        if ($is_local) {
          $target = str_replace(DIRECTORY_SEPARATOR, '/', $target);
        }

        $parts = explode('/', $target);
        $normalized_parts = array();
        while ($parts) {
          $part = array_shift($parts);
          if ($part === '' || $part === '.') {
            continue;
          }
          elseif ($part === '..' && $is_local && $normalized_parts === array()) {
            $normalized_parts[] = $part;
            break;
          }
          elseif ($part === '..') {
            array_pop($normalized_parts);
          }
          else {
            $normalized_parts[] = $part;
          }
        }

        $target = implode('/', array_merge($normalized_parts, $parts));
      }

      $uri = $scheme . '://' . $target;
    }
  }

  return $uri;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
