# ThemeRegistry::offsetGet()

- **Type:** Method
- **File:** [`includes/theme.inc`](../_file.md), lines 424–434 · [local source](../../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L424-L434)
- **Class:** [ThemeRegistry](../ThemeRegistry.md)

## Signature

```php
public function offsetGet($offset)
```

## Documentation

_No docblock in source._

## Code

```php
  public function offsetGet($offset) {
    // If the offset is set but empty, it is a registered theme hook that has
    // not yet been requested. Offsets that do not exist at all were not
    // registered in hook_theme().
    if (isset($this->storage[$offset])) {
      return $this->storage[$offset];
    }
    elseif (array_key_exists($offset, $this->storage)) {
      return $this->resolveCacheMiss($offset);
    }
  }
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
