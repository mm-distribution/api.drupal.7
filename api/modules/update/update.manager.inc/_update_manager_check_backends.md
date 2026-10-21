# _update_manager_check_backends()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 555–606 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L555-L606)
- **Module/theme:** update
- **Topics:** [update_manager_install](../../../topics/update_manager_install.md)

## Signature

```php
function _update_manager_check_backends(&$form, $operation)
```

## Documentation

```text
Checks for file transfer backends and prepares a form fragment about them.

@param array $form
  Reference to the form array we're building.
@param string $operation
  The update manager operation we're in the middle of. Can be either 'update'
  or 'install'. Use to provide operation-specific interface text.

@return
  TRUE if the update manager should continue to the next step in the
  workflow, or FALSE if we've hit a fatal configuration and must halt the
  workflow.
```

## Code

```php
function _update_manager_check_backends(&$form, $operation) {
  // If file transfers will be performed locally, we do not need to display any
  // warnings or notices to the user and should automatically continue the
  // workflow, since we won't be using a FileTransfer backend that requires
  // user input or a specific server configuration.
  if (update_manager_local_transfers_allowed()) {
    return TRUE;
  }

  // Otherwise, show the available backends.
  $form['available_backends'] = array(
    '#prefix' => '<p>',
    '#suffix' => '</p>',
  );

  $available_backends = drupal_get_filetransfer_info();
  if (empty($available_backends)) {
    if ($operation == 'update') {
      $form['available_backends']['#markup'] = t('Your server does not support updating modules and themes from this interface. Instead, update modules and themes by uploading the new versions directly to the server, as described in the <a href="@handbook_url">handbook</a>.', array('@handbook_url' => 'http://drupal.org/getting-started/install-contrib'));
    }
    else {
      $form['available_backends']['#markup'] = t('Your server does not support installing modules and themes from this interface. Instead, install modules and themes by uploading them directly to the server, as described in the <a href="@handbook_url">handbook</a>.', array('@handbook_url' => 'http://drupal.org/getting-started/install-contrib'));
    }
    return FALSE;
  }

  $backend_names = array();
  foreach ($available_backends as $backend) {
    $backend_names[] = $backend['title'];
  }
  if ($operation == 'update') {
    $form['available_backends']['#markup'] = format_plural(
      count($available_backends),
      'Updating modules and themes requires <strong>@backends access</strong> to your server. See the <a href="@handbook_url">handbook</a> for other update methods.',
      'Updating modules and themes requires access to your server via one of the following methods: <strong>@backends</strong>. See the <a href="@handbook_url">handbook</a> for other update methods.',
      array(
        '@backends' => implode(', ', $backend_names),
        '@handbook_url' => 'http://drupal.org/getting-started/install-contrib',
      ));
  }
  else {
    $form['available_backends']['#markup'] = format_plural(
      count($available_backends),
      'Installing modules and themes requires <strong>@backends access</strong> to your server. See the <a href="@handbook_url">handbook</a> for other installation methods.',
      'Installing modules and themes requires access to your server via one of the following methods: <strong>@backends</strong>. See the <a href="@handbook_url">handbook</a> for other installation methods.',
      array(
        '@backends' => implode(', ', $backend_names),
        '@handbook_url' => 'http://drupal.org/getting-started/install-contrib',
      ));
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
