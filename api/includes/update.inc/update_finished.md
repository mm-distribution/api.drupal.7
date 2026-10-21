# update_finished()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 1109–1127 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L1109-L1127)

## Signature

```php
function update_finished($success, $results, $operations)
```

## Documentation

```text
Implements callback_batch_finished().

Finishes the update process and stores the results for eventual display.

After the updates run, all caches are flushed. The update results are
stored into the session (for example, to be displayed on the update results
page in update.php). Additionally, if the site was off-line, now that the
update process is completed, the site is set back online.

@param $success
  Indicate that the batch API tasks were all completed successfully.
@param $results
  An array of all the results that were updated in update_do_one().
@param $operations
  A list of all the operations that had not been completed by the batch API.

@see update_batch()
```

## Code

```php
function update_finished($success, $results, $operations) {
  // Remove the D6 upgrade flag variable so that subsequent update runs do not
  // get the wrong context.
  variable_del('update_d6');

  // Clear the caches in case the data has been updated.
  drupal_flush_all_caches();

  $_SESSION['update_results'] = $results;
  $_SESSION['update_success'] = $success;
  $_SESSION['updates_remaining'] = $operations;

  // Now that the update is done, we can put the site back online if it was
  // previously in maintenance mode.
  if (isset($_SESSION['maintenance_mode']) && $_SESSION['maintenance_mode'] == FALSE) {
    variable_set('maintenance_mode', FALSE);
    unset($_SESSION['maintenance_mode']);
  }
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
