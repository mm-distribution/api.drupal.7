# ThemeRegistry::resolveCacheMiss()

- **Type:** Method
- **File:** [`includes/theme.inc`](../_file.md), lines 436–445 · [local source](../../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L436-L445)
- **Class:** [ThemeRegistry](../ThemeRegistry.md)

## Signature

```php
public function resolveCacheMiss($offset)
```

## Documentation

_No docblock in source._

## Code

```php
  public function resolveCacheMiss($offset) {
    if (!isset($this->completeRegistry)) {
      $this->completeRegistry = theme_get_registry();
    }
    $this->storage[$offset] = $this->completeRegistry[$offset];
    if ($this->persistable) {
      $this->persist($offset);
    }
    return $this->storage[$offset];
  }
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
