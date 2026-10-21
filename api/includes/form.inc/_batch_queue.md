# _batch_queue()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4842–4862 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4842-L4862)
- **Topics:** [batch](../../topics/batch.md)

## Signature

```php
function _batch_queue($batch_set)
```

## Documentation

```text
Returns a queue object for a batch set.

@param $batch_set
  The batch set.

@return
  The queue object.
```

## Code

```php
function _batch_queue($batch_set) {
  static $queues;

  // The class autoloader is not available when running update.php, so make
  // sure the files are manually included.
  if (!isset($queues)) {
    $queues = array();
    require_once DRUPAL_ROOT . '/modules/system/system.queue.inc';
    require_once DRUPAL_ROOT . '/includes/batch.queue.inc';
  }

  if (isset($batch_set['queue'])) {
    $name = $batch_set['queue']['name'];
    $class = $batch_set['queue']['class'];

    if (!isset($queues[$class][$name])) {
      $queues[$class][$name] = new $class($name);
    }
    return $queues[$class][$name];
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
