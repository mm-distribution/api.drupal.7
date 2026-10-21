# QueryAlterableInterface

- **Type:** Interface
- **File:** [`includes/database/query.inc`](_file.md), lines 166–248 · [local source](../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L166-L248)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
interface QueryAlterableInterface
```

## Documentation

```text
Interface for a query that can be manipulated via an alter hook.
```

## Methods (derived index)

- [addTag()](QueryAlterableInterface/addTag.md) — Adds a tag to a query.
- [hasTag()](QueryAlterableInterface/hasTag.md) — Determines if a given query has a given tag.
- [hasAllTags()](QueryAlterableInterface/hasAllTags.md) — Determines if a given query has all specified tags.
- [hasAnyTag()](QueryAlterableInterface/hasAnyTag.md) — Determines if a given query has any specified tag.
- [addMetaData()](QueryAlterableInterface/addMetaData.md) — Adds additional metadata to the query.
- [getMetaData()](QueryAlterableInterface/getMetaData.md) — Retrieves a given piece of metadata.

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
