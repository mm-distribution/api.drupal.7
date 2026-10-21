# FieldsOverlapException

- **Type:** Class
- **File:** [`includes/database/database.inc`](_file.md), lines 1938–1938 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1938)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class FieldsOverlapException extends Exception {}
```

## Documentation

```text
Exception thrown if an insert query specifies a field twice.

It is not allowed to specify a field as default and insert field, this
exception is thrown if that is the case.
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
