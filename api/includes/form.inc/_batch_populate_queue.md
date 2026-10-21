# _batch_populate_queue()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4812–4831 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4812-L4831)
- **Topics:** [batch](../../topics/batch.md)

## Signature

```php
function _batch_populate_queue(&$batch, $set_id)
```

## Documentation

```text
Populates a job queue with the operations of a batch set.

Depending on whether the batch is progressive or not, the BatchQueue or
BatchMemoryQueue handler classes will be used.

@param $batch
  The batch array.
@param $set_id
  The id of the set to process.

@return
  The name and class of the queue are added by reference to the batch set.
```

## Code

```php
function _batch_populate_queue(&$batch, $set_id) {
  $batch_set = &$batch['sets'][$set_id];

  if (isset($batch_set['operations'])) {
    $batch_set += array(
      'queue' => array(
        'name' => 'drupal_batch:' . $batch['id'] . ':' . $set_id,
        'class' => $batch['progressive'] ? 'BatchQueue' : 'BatchMemoryQueue',
      ),
    );

    $queue = _batch_queue($batch_set);
    $queue->createQueue();
    foreach ($batch_set['operations'] as $operation) {
      $queue->createItem($operation);
    }

    unset($batch_set['operations']);
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
