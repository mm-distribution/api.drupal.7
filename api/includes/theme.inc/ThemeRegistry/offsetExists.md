# ThemeRegistry::offsetExists()

- **Type:** Method
- **File:** [`includes/theme.inc`](../_file.md), lines 416–422 · [local source](../../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L416-L422)
- **Class:** [ThemeRegistry](../ThemeRegistry.md)

## Signature

```php
public function offsetExists($offset)
```

## Documentation

_No docblock in source._

## Code

```php
  public function offsetExists($offset) {
    // Since the theme registry allows for theme hooks to be requested that
    // are not registered, just check the existence of the key in the registry.
    // Use array_key_exists() here since a NULL value indicates that the theme
    // hook exists but has not yet been requested.
    return isset($this->storage[$offset]) || array_key_exists($offset, $this->storage);
  }
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
