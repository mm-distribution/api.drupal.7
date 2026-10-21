# update_manager_install_form_submit()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 641–747 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L641-L747)
- **Module/theme:** update
- **Topics:** [update_manager_install](../../../topics/update_manager_install.md)

## Signature

```php
function update_manager_install_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for update_manager_install_form().

Either downloads the file specified in the URL to a temporary cache, or
uploads the file attached to the form, then attempts to extract the archive
into a temporary location and verify it. Instantiate the appropriate
Updater class for this project and make sure it is not already installed in
the live webroot. If everything is successful, setup an operation to run
via authorize.php which will copy the extracted files from the temporary
location into the live site.

@see update_manager_install_form_validate()
@see update_authorize_run_install()
@see system_authorized_init()
@see system_authorized_get_url()
```

## Code

```php
function update_manager_install_form_submit($form, &$form_state) {
  if ($form_state['values']['project_url']) {
    $field = 'project_url';
    $local_cache = update_manager_file_get($form_state['values']['project_url']);
    if (!$local_cache) {
      form_set_error($field, t('Unable to retrieve Drupal project from %url.', array('%url' => $form_state['values']['project_url'])));
      return;
    }
  }
  elseif ($_FILES['files']['name']['project_upload']) {
    $validators = array('file_validate_extensions' => array(archiver_get_extensions()));
    $field = 'project_upload';
    if (!($finfo = file_save_upload($field, $validators, NULL, FILE_EXISTS_REPLACE))) {
      // Failed to upload the file. file_save_upload() calls form_set_error() on
      // failure.
      return;
    }
    $local_cache = $finfo->uri;
  }

  $directory = _update_manager_extract_directory();
  try {
    $archive = update_manager_archive_extract($local_cache, $directory);
  }
  catch (Exception $e) {
    form_set_error($field, $e->getMessage());
    return;
  }

  $files = $archive->listContents();
  if (!$files) {
    form_set_error($field, t('Provided archive contains no files.'));
    return;
  }

  // Unfortunately, we can only use the directory name to determine the project
  // name. Some archivers list the first file as the directory (i.e., MODULE/)
  // and others list an actual file (i.e., MODULE/README.TXT).
  $project = strtok($files[0], '/\\');

  $archive_errors = update_manager_archive_verify($project, $local_cache, $directory);
  if (!empty($archive_errors)) {
    form_set_error($field, array_shift($archive_errors));
    // @todo: Fix me in D8: We need a way to set multiple errors on the same
    // form element and have all of them appear!
    if (!empty($archive_errors)) {
      foreach ($archive_errors as $error) {
        drupal_set_message($error, 'error');
      }
    }
    return;
  }

  // Make sure the Updater registry is loaded.
  drupal_get_updaters();

  $project_location = $directory . '/' . $project;
  try {
    $updater = Updater::factory($project_location);
  }
  catch (Exception $e) {
    form_set_error($field, $e->getMessage());
    return;
  }

  try {
    $project_title = Updater::getProjectTitle($project_location);
  }
  catch (Exception $e) {
    form_set_error($field, $e->getMessage());
    return;
  }

  if (!$project_title) {
    form_set_error($field, t('Unable to determine %project name.', array('%project' => $project)));
  }

  if ($updater->isInstalled()) {
    form_set_error($field, t('%project is already installed.', array('%project' => $project_title)));
    return;
  }

  $project_real_location = drupal_realpath($project_location);
  $arguments = array(
    'project' => $project,
    'updater_name' => get_class($updater),
    'local_url' => $project_real_location,
  );

  // If the owner of the directory we extracted is the same as the
  // owner of our configuration directory (e.g. sites/default) where we're
  // trying to install the code, there's no need to prompt for FTP/SSH
  // credentials. Instead, we instantiate a FileTransferLocal and invoke
  // update_authorize_run_install() directly.
  if (fileowner($project_real_location) == fileowner(conf_path())) {
    module_load_include('inc', 'update', 'update.authorize');
    $filetransfer = new FileTransferLocal(DRUPAL_ROOT);
    call_user_func_array('update_authorize_run_install', array_merge(array($filetransfer), $arguments));
  }
  // Otherwise, go through the regular workflow to prompt for FTP/SSH
  // credentials and invoke update_authorize_run_install() indirectly with
  // whatever FileTransfer object authorize.php creates for us.
  else {
    system_authorized_init('update_authorize_run_install', drupal_get_path('module', 'update') . '/update.authorize.inc', $arguments, t('Update manager'));
    $form_state['redirect'] = system_authorized_get_url();
  }
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
