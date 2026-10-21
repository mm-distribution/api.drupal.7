# SchemaCache::resolveCacheMiss()

- **Type:** Method
- **File:** [`includes/bootstrap.inc`](../_file.md), lines 3397–3403 · [local source](../../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3397-L3403)
- **Class:** [SchemaCache](../SchemaCache.md)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
protected function resolveCacheMiss($offset)
```

## Documentation

```text
Overrides DrupalCacheArray::resolveCacheMiss().
```

## Code

```php
  protected function resolveCacheMiss($offset) {
    $complete_schema = drupal_get_complete_schema();
    $value = isset($complete_schema[$offset]) ? $complete_schema[$offset] :  NULL;
    $this->storage[$offset] = $value;
    $this->persist($offset);
    return $value;
  }
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
