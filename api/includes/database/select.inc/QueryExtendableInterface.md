# QueryExtendableInterface

- **Type:** Interface
- **File:** [`includes/database/select.inc`](_file.md), lines 20–34 · [local source](../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L20-L34)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
interface QueryExtendableInterface
```

## Documentation

```text
Interface for extendable query objects.

"Extenders" follow the "Decorator" OOP design pattern.  That is, they wrap
and "decorate" another object.  In our case, they implement the same interface
as select queries and wrap a select query, to which they delegate almost all
operations.  Subclasses of this class may implement additional methods or
override existing methods as appropriate.  Extenders may also wrap other
extender objects, allowing for arbitrarily complex "enhanced" queries.
```

## Methods (derived index)

- [extend()](QueryExtendableInterface/extend.md) — Enhance this object by wrapping it in an extender object.

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
