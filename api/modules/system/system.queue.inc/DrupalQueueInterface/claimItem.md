# DrupalQueueInterface::claimItem()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 148–148 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L148)
- **Class:** [DrupalQueueInterface](../DrupalQueueInterface.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function claimItem($lease_time = 3600);
```

## Documentation

```text
Claim an item in the queue for processing.

@param $lease_time
  How long the processing is expected to take in seconds, defaults to an
  hour. After this lease expires, the item will be reset and another
  consumer can claim the item. For idempotent tasks (which can be run
  multiple times without side effects), shorter lease times would result
  in lower latency in case a consumer fails. For tasks that should not be
  run more than once (non-idempotent), a larger lease time will make it
  more rare for a given task to run multiple times in cases of failure,
  at the cost of higher latency.
@return
  On success we return an item object. If the queue is unable to claim an
  item it returns false. This implies a best effort to retrieve an item
  and either the queue is empty or there is some other non-recoverable
  problem.
```

## Code

```php
  public function claimItem($lease_time = 3600);
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
