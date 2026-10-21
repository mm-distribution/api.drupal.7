# SchemaCache::__construct()

- **Type:** Method
- **File:** [`includes/bootstrap.inc`](../_file.md), lines 3389–3392 · [local source](../../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3389-L3392)
- **Class:** [SchemaCache](../SchemaCache.md)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
public function __construct()
```

## Documentation

```text
Constructs a SchemaCache object.
```

## Code

```php
  public function __construct() {
    // Cache by request method.
    parent::__construct('schema:runtime:' . ($_SERVER['REQUEST_METHOD'] == 'GET'), 'cache');
  }
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
