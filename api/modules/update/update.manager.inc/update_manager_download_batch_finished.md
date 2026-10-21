# update_manager_download_batch_finished()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 347–365 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L347-L365)
- **Module/theme:** update
- **Topics:** [update_manager_update](../../../topics/update_manager_update.md)

## Signature

```php
function update_manager_download_batch_finished($success, $results)
```

## Documentation

```text
Implements callback_batch_finished().

Batch callback: Performs actions when the download batch is completed.

@param $success
  TRUE if the batch operation was successful, FALSE if there were errors.
@param $results
  An associative array of results from the batch operation.
```

## Code

```php
function update_manager_download_batch_finished($success, $results) {
  if (!empty($results['errors'])) {
    $error_list = array(
      'title' => t('Downloading updates failed:'),
      'items' => $results['errors'],
    );
    drupal_set_message(theme('item_list', $error_list), 'error');
  }
  elseif ($success) {
    drupal_set_message(t('Updates downloaded successfully.'));
    $_SESSION['update_manager_update_projects'] = $results['projects'];
    drupal_goto('admin/update/ready');
  }
  else {
    // Ideally we're catching all Exceptions, so they should never see this,
    // but just in case, we have to tell them something.
    drupal_set_message(t('Fatal error trying to download.'), 'error');
  }
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
