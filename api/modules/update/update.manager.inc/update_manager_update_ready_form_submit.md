# update_manager_update_ready_form_submit()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 423–469 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L423-L469)
- **Module/theme:** update
- **Topics:** [update_manager_update](../../../topics/update_manager_update.md)

## Signature

```php
function update_manager_update_ready_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for update_manager_update_ready_form().

If the site administrator requested that the site is put offline during the
update, do so now. Otherwise, pull information about all the required updates
out of the SESSION, figure out what Drupal\Core\Updater\Updater class is
needed for each one, generate an array of update operations to perform, and
hand it all off to system_authorized_init(), then redirect to authorize.php.

@see update_authorize_run_update()
@see system_authorized_init()
@see system_authorized_get_url()
```

## Code

```php
function update_manager_update_ready_form_submit($form, &$form_state) {
  // Store maintenance_mode setting so we can restore it when done.
  $_SESSION['maintenance_mode'] = variable_get('maintenance_mode', FALSE);
  if ($form_state['values']['maintenance_mode'] == TRUE) {
    variable_set('maintenance_mode', TRUE);
  }

  if (!empty($_SESSION['update_manager_update_projects'])) {
    // Make sure the Updater registry is loaded.
    drupal_get_updaters();

    $updates = array();
    $directory = _update_manager_extract_directory();

    $projects = $_SESSION['update_manager_update_projects'];
    unset($_SESSION['update_manager_update_projects']);

    foreach ($projects as $project => $url) {
      $project_location = $directory . '/' . $project;
      $updater = Updater::factory($project_location);
      $project_real_location = drupal_realpath($project_location);
      $updates[] = array(
        'project' => $project,
        'updater_name' => get_class($updater),
        'local_url' => $project_real_location,
      );
    }

    // If the owner of the last directory we extracted is the same as the
    // owner of our configuration directory (e.g. sites/default) where we're
    // trying to install the code, there's no need to prompt for FTP/SSH
    // credentials. Instead, we instantiate a FileTransferLocal and invoke
    // update_authorize_run_update() directly.
    if (fileowner($project_real_location) == fileowner(conf_path())) {
      module_load_include('inc', 'update', 'update.authorize');
      $filetransfer = new FileTransferLocal(DRUPAL_ROOT);
      update_authorize_run_update($filetransfer, $updates);
    }
    // Otherwise, go through the regular workflow to prompt for FTP/SSH
    // credentials and invoke update_authorize_run_update() indirectly with
    // whatever FileTransfer object authorize.php creates for us.
    else {
      system_authorized_init('update_authorize_run_update', drupal_get_path('module', 'update') . '/update.authorize.inc', array($updates), t('Update manager'));
      $form_state['redirect'] = system_authorized_get_url();
    }
  }
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
