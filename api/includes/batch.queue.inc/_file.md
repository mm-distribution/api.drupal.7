# includes/batch.queue.inc

- **Source:** [local](../../../source/includes/batch.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc) · 85 lines

## File documentation

```text
@file
Queue handlers used by the Batch API.

These implementations:
- Ensure FIFO ordering.
- Allow an item to be repeatedly claimed until it is actually deleted (no
  notion of lease time or 'expire' date), to allow multipass operations.
```

## Classes and interfaces (derived index)

- [BatchQueue](BatchQueue.md) — Defines a batch queue.
- [BatchMemoryQueue](BatchMemoryQueue.md) — Defines a batch queue for non-progressive batches.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
