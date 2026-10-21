# QueueTestCase::testQueue()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2131–2189 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2131-L2189)
- **Class:** [QueueTestCase](../QueueTestCase.md)
- **Module/theme:** system

## Signature

```php
function testQueue()
```

## Documentation

```text
Queues and dequeues a set of items to check the basic queue functionality.
```

## Code

```php
  function testQueue() {
    // Create two queues.
    $queue1 = DrupalQueue::get($this->randomName());
    $queue1->createQueue();
    $queue2 = DrupalQueue::get($this->randomName());
    $queue2->createQueue();

    // Create four items.
    $data = array();
    for ($i = 0; $i < 4; $i++) {
      $data[] = array($this->randomName() => $this->randomName());
    }

    // Queue items 1 and 2 in the queue1.
    $queue1->createItem($data[0]);
    $queue1->createItem($data[1]);

    // Retrieve two items from queue1.
    $items = array();
    $new_items = array();

    $items[] = $item = $queue1->claimItem();
    $new_items[] = $item->data;

    $items[] = $item = $queue1->claimItem();
    $new_items[] = $item->data;

    // First two dequeued items should match the first two items we queued.
    $this->assertEqual($this->queueScore($data, $new_items), 2, 'Two items matched');

    // Add two more items.
    $queue1->createItem($data[2]);
    $queue1->createItem($data[3]);

    $this->assertTrue($queue1->numberOfItems(), 'Queue 1 is not empty after adding items.');
    $this->assertFalse($queue2->numberOfItems(), 'Queue 2 is empty while Queue 1 has items');

    $items[] = $item = $queue1->claimItem();
    $new_items[] = $item->data;

    $items[] = $item = $queue1->claimItem();
    $new_items[] = $item->data;

    // All dequeued items should match the items we queued exactly once,
    // therefore the score must be exactly 4.
    $this->assertEqual($this->queueScore($data, $new_items), 4, 'Four items matched');

    // There should be no duplicate items.
    $this->assertEqual($this->queueScore($new_items, $new_items), 4, 'Four items matched');

    // Delete all items from queue1.
    foreach ($items as $item) {
      $queue1->deleteItem($item);
    }

    // Check that both queues are empty.
    $this->assertFalse($queue1->numberOfItems(), 'Queue 1 is empty');
    $this->assertFalse($queue2->numberOfItems(), 'Queue 2 is empty');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
