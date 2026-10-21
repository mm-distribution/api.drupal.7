# update_authorize_run_install()

- **Type:** Function
- **File:** [`modules/update/update.authorize.inc`](_file.md), lines 73–97 · [local source](../../../../source/modules/update/update.authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc#L73-L97)
- **Module/theme:** update

## Signature

```php
function update_authorize_run_install($filetransfer, $project, $updater_name, $local_url)
```

## Documentation

```text
Installs a new project when invoked by authorize.php.

Callback for system_authorized_init() in
update_manager_install_form_submit().

@param FileTransfer $filetransfer
  The FileTransfer object created by authorize.php for use during this
  operation.
@param string $project
  The canonical project short name (e.g., {system}.name).
@param string $updater_name
  The name of the Updater class to use for installing this project.
@param string $local_url
  The URL to the locally installed temp directory where the project has
  already been downloaded and extracted into.
```

## Code

```php
function update_authorize_run_install($filetransfer, $project, $updater_name, $local_url) {
  $operations[] = array(
    'update_authorize_batch_copy_project',
    array(
      $project,
      $updater_name,
      $local_url,
      $filetransfer,
    ),
  );

  // @todo Instantiate our Updater to set the human-readable title?
  $batch = array(
    'title' => t('Installing %project', array('%project' => $project)),
    'init_message' => t('Preparing to install'),
    'operations' => $operations,
    // @todo Use a different finished callback for different messages?
    'finished' => 'update_authorize_install_batch_finished',
    'file' => drupal_get_path('module', 'update') . '/update.authorize.inc',
  );
  batch_set($batch);

  // Invoke the batch via authorize.php.
  system_authorized_batch_process();
}
```

---
_Drupal 7.103 · [modules/update/update.authorize.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
