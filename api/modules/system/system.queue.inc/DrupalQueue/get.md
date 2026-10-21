# DrupalQueue::get()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 81–96 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L81-L96)
- **Class:** [DrupalQueue](../DrupalQueue.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public static function get($name, $reliable = FALSE)
```

## Documentation

```text
Returns the queue object for a given name.

The following variables can be set by variable_set or $conf overrides:
- queue_class_$name: the class to be used for the queue $name.
- queue_default_class: the class to use when queue_class_$name is not
  defined. Defaults to SystemQueue, a reliable backend using SQL.
- queue_default_reliable_class: the class to use when queue_class_$name is
  not defined and the queue_default_class is not reliable. Defaults to
  SystemQueue.

@param $name
  Arbitrary string. The name of the queue to work with.
@param $reliable
  TRUE if the ordering of items and guaranteeing every item executes at
  least once is important, FALSE if scalability is the main concern.

@return
  The queue object for a given name.
```

## Code

```php
  public static function get($name, $reliable = FALSE) {
    static $queues;
    if (!isset($queues[$name])) {
      $class = variable_get('queue_class_' . $name, NULL);
      if (!$class) {
        $class = variable_get('queue_default_class', 'SystemQueue');
      }
      $object = new $class($name);
      if ($reliable && !$object instanceof DrupalReliableQueueInterface) {
        $class = variable_get('queue_default_reliable_class', 'SystemQueue');
        $object = new $class($name);
      }
      $queues[$name] = $object;
    }
    return $queues[$name];
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
