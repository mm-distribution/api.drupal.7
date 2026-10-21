# update_manager_update_form_submit()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 310–335 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L310-L335)
- **Module/theme:** update
- **Topics:** [update_manager_update](../../../topics/update_manager_update.md)

## Signature

```php
function update_manager_update_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for update_manager_update_form().

Sets up a batch that downloads, extracts, and verifies the selected releases.

@see update_manager_update_form_validate()
```

## Code

```php
function update_manager_update_form_submit($form, &$form_state) {
  $projects = array();
  foreach (array('projects', 'disabled_projects') as $type) {
    if (!empty($form_state['values'][$type])) {
      $projects = array_merge($projects, array_keys(array_filter($form_state['values'][$type])));
    }
  }
  $operations = array();
  foreach ($projects as $project) {
    $operations[] = array(
      'update_manager_batch_project_get',
      array(
        $project,
        $form_state['values']['project_downloads'][$project],
      ),
    );
  }
  $batch = array(
    'title' => t('Downloading updates'),
    'init_message' => t('Preparing to download selected updates'),
    'operations' => $operations,
    'finished' => 'update_manager_download_batch_finished',
    'file' => drupal_get_path('module', 'update') . '/update.manager.inc',
  );
  batch_set($batch);
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
