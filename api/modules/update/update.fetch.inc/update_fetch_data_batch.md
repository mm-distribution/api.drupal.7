# update_fetch_data_batch()

- **Type:** Function
- **File:** [`modules/update/update.fetch.inc`](_file.md), lines 39–79 · [local source](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc#L39-L79)
- **Module/theme:** update

## Signature

```php
function update_fetch_data_batch(&$context)
```

## Documentation

```text
Implements callback_batch_operation().

Processes a step in batch for fetching available update data.

@param $context
  Reference to an array used for Batch API storage.
```

## Code

```php
function update_fetch_data_batch(&$context) {
  $queue = DrupalQueue::get('update_fetch_tasks');
  if (empty($context['sandbox']['max'])) {
    $context['finished'] = 0;
    $context['sandbox']['max'] = $queue->numberOfItems();
    $context['sandbox']['progress'] = 0;
    $context['message'] = t('Checking available update data ...');
    $context['results']['updated'] = 0;
    $context['results']['failures'] = 0;
    $context['results']['processed'] = 0;
  }

  // Grab another item from the fetch queue.
  for ($i = 0; $i < 5; $i++) {
    if ($item = $queue->claimItem()) {
      if (_update_process_fetch_task($item->data)) {
        $context['results']['updated']++;
        $context['message'] = t('Checked available update data for %title.', array('%title' => $item->data['info']['name']));
      }
      else {
        $context['message'] = t('Failed to check available update data for %title.', array('%title' => $item->data['info']['name']));
        $context['results']['failures']++;
      }
      $context['sandbox']['progress']++;
      $context['results']['processed']++;
      $context['finished'] = $context['sandbox']['progress'] / $context['sandbox']['max'];
      $queue->deleteItem($item);
    }
    else {
      // If the queue is currently empty, we're done. It's possible that
      // another thread might have added new fetch tasks while we were
      // processing this batch. In that case, the usual 'finished' math could
      // get confused, since we'd end up processing more tasks that we thought
      // we had when we started and initialized 'max' with numberOfItems(). By
      // forcing 'finished' to be exactly 1 here, we ensure that batch
      // processing is terminated.
      $context['finished'] = 1;
      return;
    }
  }
}
```

---
_Drupal 7.103 · [modules/update/update.fetch.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
