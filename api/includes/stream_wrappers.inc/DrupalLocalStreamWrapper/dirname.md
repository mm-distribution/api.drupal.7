# DrupalLocalStreamWrapper::dirname()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 754–764 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L754-L764)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function dirname($uri = NULL)
```

## Documentation

```text
Gets the name of the directory from a given path.

This method is usually accessed through drupal_dirname(), which wraps
around the PHP dirname() function because it does not support stream
wrappers.

@param $uri
  A URI or path.

@return
  A string containing the directory name.

@see drupal_dirname()
```

## Code

```php
  public function dirname($uri = NULL) {
    list($scheme, $target) = explode('://', $uri, 2);
    $target  = $this->getTarget($uri);
    $dirname = dirname($target);

    if ($dirname == '.') {
      $dirname = '';
    }

    return $scheme . '://' . $dirname;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
