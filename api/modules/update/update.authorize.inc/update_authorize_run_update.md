# update_authorize_run_update()

- **Type:** Function
- **File:** [`modules/update/update.authorize.inc`](_file.md), lines 29–54 · [local source](../../../../source/modules/update/update.authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc#L29-L54)
- **Module/theme:** update

## Signature

```php
function update_authorize_run_update($filetransfer, $projects)
```

## Documentation

```text
Updates existing projects when invoked by authorize.php.

Callback for system_authorized_init() in
update_manager_update_ready_form_submit().

@param $filetransfer
  The FileTransfer object created by authorize.php for use during this
  operation.
@param $projects
  A nested array of projects to install into the live webroot, keyed by
  project name. Each subarray contains the following keys:
  - project: The canonical project short name.
  - updater_name: The name of the Updater class to use for this project.
  - local_url: The locally installed location of new code to update with.
```

## Code

```php
function update_authorize_run_update($filetransfer, $projects) {
  $operations = array();
  foreach ($projects as $project => $project_info) {
    $operations[] = array(
      'update_authorize_batch_copy_project',
      array(
        $project_info['project'],
        $project_info['updater_name'],
        $project_info['local_url'],
        $filetransfer,
      ),
    );
  }

  $batch = array(
    'title' => t('Installing updates'),
    'init_message' => t('Preparing to update your site'),
    'operations' => $operations,
    'finished' => 'update_authorize_update_batch_finished',
    'file' => drupal_get_path('module', 'update') . '/update.authorize.inc',
  );

  batch_set($batch);
  // Invoke the batch via authorize.php.
  system_authorized_batch_process();
}
```

---
_Drupal 7.103 · [modules/update/update.authorize.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
