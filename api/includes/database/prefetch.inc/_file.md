# includes/database/prefetch.inc

- **Source:** [local](../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · 522 lines

## File documentation

```text
@file
Database interface code for engines that need complete control over their
result sets. For example, SQLite will prefix some column names by the name
of the table. We post-process the data, by renaming the column names
using the same convention as MySQL and PostgreSQL.
```

## Classes and interfaces (derived index)

- [DatabaseStatementPrefetch](DatabaseStatementPrefetch.md) — An implementation of DatabaseStatementInterface that prefetches all data.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
