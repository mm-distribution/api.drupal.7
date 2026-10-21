# UpdateCoreTestCase::testFetchTasks()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 241–263 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L241-L263)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
function testFetchTasks()
```

## Documentation

```text
Tests that exactly one fetch task per project is created and not more.
```

## Code

```php
  function testFetchTasks() {
    $projecta = array(
      'name' => 'aaa_update_test',
    );
    $projectb = array(
      'name' => 'bbb_update_test',
    );
    $queue = DrupalQueue::get('update_fetch_tasks');
    $this->assertEqual($queue->numberOfItems(), 0, 'Queue is empty');
    update_create_fetch_task($projecta);
    $this->assertEqual($queue->numberOfItems(), 1, 'Queue contains one item');
    update_create_fetch_task($projectb);
    $this->assertEqual($queue->numberOfItems(), 2, 'Queue contains two items');
    // Try to add project a again.
    update_create_fetch_task($projecta);
    $this->assertEqual($queue->numberOfItems(), 2, 'Queue still contains two items');

    // Clear cache and try again.
    _update_cache_clear();
    drupal_static_reset('_update_create_fetch_task');
    update_create_fetch_task($projecta);
    $this->assertEqual($queue->numberOfItems(), 2, 'Queue contains two items');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
