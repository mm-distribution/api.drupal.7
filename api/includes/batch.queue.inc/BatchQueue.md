# BatchQueue

- **Type:** Class
- **File:** [`includes/batch.queue.inc`](_file.md), lines 19–50 · [local source](../../../source/includes/batch.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc#L19-L50)

## Signature

```php
class BatchQueue extends SystemQueue
```

## Documentation

```text
Defines a batch queue.

Stale items from failed batches are cleaned from the {queue} table on cron
using the 'created' date.
```

## Methods (derived index)

- [claimItem()](BatchQueue/claimItem.md) — Overrides SystemQueue::claimItem().
- [getAllItems()](BatchQueue/getAllItems.md) — Retrieves all remaining items in the queue.

---
_Drupal 7.103 · [includes/batch.queue.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
