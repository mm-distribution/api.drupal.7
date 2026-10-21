# hook_update_status_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/update/update.api.php`](_file.md), lines 85–103 · [local source](../../../../source/modules/update/update.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.api.php#L85-L103)
- **Module/theme:** update
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_update_status_alter(&$projects)
```

## Documentation

```text
Alter the information about available updates for projects.

@param $projects
  Reference to an array of information about available updates to each
  project installed on the system.

@see update_calculate_project_data()
```

## Code

```php
function hook_update_status_alter(&$projects) {
  $settings = variable_get('update_advanced_project_settings', array());
  foreach ($projects as $project => $project_info) {
    if (isset($settings[$project]) && isset($settings[$project]['check']) &&
        ($settings[$project]['check'] == 'never' ||
          (isset($project_info['recommended']) &&
            $settings[$project]['check'] === $project_info['recommended']))) {
      $projects[$project]['status'] = UPDATE_NOT_CHECKED;
      $projects[$project]['reason'] = t('Ignored from settings');
      if (!empty($settings[$project]['notes'])) {
        $projects[$project]['extra'][] = array(
          'class' => array('admin-note'),
          'label' => t('Administrator note'),
          'data' => $settings[$project]['notes'],
        );
      }
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_update_status_alter()".

- [update_test_update_status_alter()](../tests/update_test.module/update_test_update_status_alter.md) — `modules/update/tests/update_test.module`

---
_Drupal 7.103 · [modules/update/update.api.php](https://github.com/drupal/drupal/blob/7.103/modules/update/update.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
