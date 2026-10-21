# _update_requirement_check()

- **Type:** Function
- **File:** [`modules/update/update.install`](_file.md), lines 117–159 · [local source](../../../../source/modules/update/update.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install#L117-L159)
- **Module/theme:** update

## Signature

```php
function _update_requirement_check($project, $type)
```

## Documentation

```text
Fills in the requirements array.

This is shared for both core and contrib to generate the right elements in
the array for hook_requirements().

@param $project
  Array of information about the project we're testing as returned by
  update_calculate_project_data().
@param $type
  What kind of project this is ('core' or 'contrib').

@return
  An array to be included in the nested $requirements array.

@see hook_requirements()
@see update_requirements()
@see update_calculate_project_data()
```

## Code

```php
function _update_requirement_check($project, $type) {
  $requirement = array();
  if ($type == 'core') {
    $requirement['title'] = t('Drupal core update status');
  }
  else {
    $requirement['title'] = t('Module and theme update status');
  }
  $status = $project['status'];
  if ($status != UPDATE_CURRENT) {
    $requirement['reason'] = $status;
    $requirement['description'] = _update_message_text($type, $status, TRUE);
    $requirement['severity'] = REQUIREMENT_ERROR;
  }
  switch ($status) {
    case UPDATE_NOT_SECURE:
      $requirement_label = t('Not secure!');
      break;
    case UPDATE_REVOKED:
      $requirement_label = t('Revoked!');
      break;
    case UPDATE_NOT_SUPPORTED:
      $requirement_label = t('Unsupported release');
      break;
    case UPDATE_NOT_CURRENT:
      $requirement_label = t('Out of date');
      $requirement['severity'] = REQUIREMENT_WARNING;
      break;
    case UPDATE_UNKNOWN:
    case UPDATE_NOT_CHECKED:
    case UPDATE_NOT_FETCHED:
      $requirement_label = isset($project['reason']) ? $project['reason'] : t('Can not determine status');
      $requirement['severity'] = REQUIREMENT_WARNING;
      break;
    default:
      $requirement_label = t('Up to date');
  }
  if ($status != UPDATE_CURRENT && $type == 'core' && isset($project['recommended'])) {
    $requirement_label .= ' ' . t('(version @version available)', array('@version' => $project['recommended']));
  }
  $requirement['value'] = l($requirement_label, update_manager_access() ? 'admin/reports/updates/update' : 'admin/reports/updates');
  return $requirement;
}
```

---
_Drupal 7.103 · [modules/update/update.install](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install) · Licensed GPL-2.0-or-later (see LICENSE)._
