# _update_create_fetch_task()

- **Type:** Function
- **File:** [`modules/update/update.fetch.inc`](_file.md), lines 246–273 · [local source](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc#L246-L273)
- **Module/theme:** update

## Signature

```php
function _update_create_fetch_task($project)
```

## Documentation

```text
Adds a task to the queue for fetching release history data for a project.

We only create a new fetch task if there's no task already in the queue for
this particular project (based on 'fetch_task::' entries in the
{cache_update} table).

@param $project
  Associative array of information about a project as created by
  update_get_projects(), including keys such as 'name' (short name), and the
  'info' array with data from a .info file for the project.

@see update_get_projects()
@see update_get_available()
@see update_refresh()
@see update_fetch_data()
@see _update_process_fetch_task()
```

## Code

```php
function _update_create_fetch_task($project) {
  $fetch_tasks = &drupal_static(__FUNCTION__, array());
  if (empty($fetch_tasks)) {
    $fetch_tasks = _update_get_cache_multiple('fetch_task');
  }
  $cid = 'fetch_task::' . $project['name'];
  if (empty($fetch_tasks[$cid])) {
    $queue = DrupalQueue::get('update_fetch_tasks');
    $queue->createItem($project);
    // Due to race conditions, it is possible that another process already
    // inserted a row into the {cache_update} table and the following query will
    // throw an exception.
    // @todo: Remove the need for the manual check by relying on a queue that
    // enforces unique items.
    try {
      db_insert('cache_update')
        ->fields(array(
          'cid' => $cid,
          'created' => REQUEST_TIME,
        ))
        ->execute();
    }
    catch (Exception $e) {
      // The exception can be ignored safely.
    }
    $fetch_tasks[$cid] = REQUEST_TIME;
  }
}
```

---
_Drupal 7.103 · [modules/update/update.fetch.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
