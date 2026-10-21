# update_update_7000()

- **Type:** Function
- **File:** [`modules/update/update.install`](_file.md), lines 169–173 · [local source](../../../../source/modules/update/update.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install#L169-L173)
- **Module/theme:** update
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function update_update_7000()
```

## Documentation

```text
Create a queue to store tasks for requests to fetch available update data.
```

## Code

```php
function update_update_7000() {
  module_load_include('inc', 'system', 'system.queue');
  $queue = DrupalQueue::get('update_fetch_tasks');
  $queue->createQueue();
}
```

---
_Drupal 7.103 · [modules/update/update.install](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install) · Licensed GPL-2.0-or-later (see LICENSE)._
