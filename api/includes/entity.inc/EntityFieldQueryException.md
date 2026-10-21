# EntityFieldQueryException

- **Type:** Class
- **File:** [`includes/entity.inc`](_file.md), lines 445–445 · [local source](../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L445)

## Signature

```php
class EntityFieldQueryException extends Exception {}
```

## Documentation

```text
Exception thrown by EntityFieldQuery() on unsupported query syntax.

Some storage modules might not support the full range of the syntax for
conditions, and will raise an EntityFieldQueryException when an unsupported
condition was specified.
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
