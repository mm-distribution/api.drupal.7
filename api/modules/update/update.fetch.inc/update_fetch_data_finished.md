# update_fetch_data_finished()

- **Type:** Function
- **File:** [`modules/update/update.fetch.inc`](_file.md), lines 93–107 · [local source](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc#L93-L107)
- **Module/theme:** update

## Signature

```php
function update_fetch_data_finished($success, $results)
```

## Documentation

```text
Implements callback_batch_finished().

Performs actions when all fetch tasks have been completed.

@param $success
  TRUE if the batch operation was successful; FALSE if there were errors.
@param $results
  An associative array of results from the batch operation, including the key
  'updated' which holds the total number of projects we fetched available
  update data for.
```

## Code

```php
function update_fetch_data_finished($success, $results) {
  if ($success) {
    if (!empty($results)) {
      if (!empty($results['updated'])) {
        drupal_set_message(format_plural($results['updated'], 'Checked available update data for one project.', 'Checked available update data for @count projects.'));
      }
      if (!empty($results['failures'])) {
        drupal_set_message(format_plural($results['failures'], 'Failed to get available update data for one project.', 'Failed to get available update data for @count projects.'), 'error');
      }
    }
  }
  else {
    drupal_set_message(t('An error occurred trying to get available update data.'), 'error');
  }
}
```

---
_Drupal 7.103 · [modules/update/update.fetch.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
