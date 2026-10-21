# update_authorize_install_batch_finished()

- **Type:** Function
- **File:** [`modules/update/update.authorize.inc`](_file.md), lines 255–300 · [local source](../../../../source/modules/update/update.authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc#L255-L300)
- **Module/theme:** update

## Signature

```php
function update_authorize_install_batch_finished($success, $results)
```

## Documentation

```text
Implements callback_batch_finished().

Performs actions when the authorized install batch is done.

This processes the results and stashes them into SESSION such that
authorize.php will render a report. Also responsible for putting the site
back online after a successful install if necessary.

@param $success
  TRUE if the batch operation was a success; FALSE if there were errors.
@param $results
  An associative array of results from the batch operation.
```

## Code

```php
function update_authorize_install_batch_finished($success, $results) {
  foreach ($results['log'] as $project => $messages) {
    if (!empty($messages['#abort'])) {
      $success = FALSE;
    }
  }
  $offline = variable_get('maintenance_mode', FALSE);
  if ($success) {
    // Take the site out of maintenance mode if it was previously that way.
    if ($offline && isset($_SESSION['maintenance_mode']) && $_SESSION['maintenance_mode'] == FALSE) {
      variable_set('maintenance_mode', FALSE);
      $page_message = array(
        'message' => t('Installation was completed successfully. Your site has been taken out of maintenance mode.'),
        'type' => 'status',
      );
    }
    else {
      $page_message = array(
        'message' => t('Installation was completed successfully.'),
        'type' => 'status',
      );
    }
  }
  elseif (!$success && !$offline) {
    $page_message = array(
      'message' => t('Installation failed! See the log below for more information.'),
      'type' => 'error',
    );
  }
  else {
    $page_message = array(
      'message' => t('Installation failed! See the log below for more information. Your site is still in maintenance mode.'),
      'type' => 'error',
    );
  }

  // Unset the variable since it is no longer needed.
  unset($_SESSION['maintenance_mode']);

  // Set all these values into the SESSION so authorize.php can display them.
  $_SESSION['authorize_results']['success'] = $success;
  $_SESSION['authorize_results']['page_message'] = $page_message;
  $_SESSION['authorize_results']['messages'] = $results['log'];
  $_SESSION['authorize_results']['tasks'] = $results['tasks'];
  $_SESSION['authorize_operation']['page_title'] = t('Update manager');
}
```

---
_Drupal 7.103 · [modules/update/update.authorize.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
