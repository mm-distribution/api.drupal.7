# update_requirements()

- **Type:** Function
- **File:** [`modules/update/update.install`](_file.md), lines 28–57 · [local source](../../../../source/modules/update/update.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install#L28-L57)
- **Module/theme:** update
- **Implements:** [hook_requirements()](../../system/system.api.php/hook_requirements.md)

## Signature

```php
function update_requirements($phase)
```

## Documentation

```text
Implements hook_requirements().

@return
  An array describing the status of the site regarding available updates. If
  there is no update data, only one record will be returned, indicating that
  the status of core can't be determined. If data is available, there will be
  two records: one for core, and another for all of contrib (assuming there
  are any contributed modules or themes enabled on the site). In addition to
  the fields expected by hook_requirements ('value', 'severity', and
  optionally 'description'), this array will contain a 'reason' attribute,
  which is an integer constant to indicate why the given status is being
  returned (UPDATE_NOT_SECURE, UPDATE_NOT_CURRENT, or UPDATE_UNKNOWN). This
  is used for generating the appropriate e-mail notification messages during
  update_cron(), and might be useful for other modules that invoke
  update_requirements() to find out if the site is up to date or not.

@see _update_message_text()
@see _update_cron_notify()
```

## Code

```php
function update_requirements($phase) {
  $requirements = array();
  if ($phase == 'runtime') {
    if ($available = update_get_available(FALSE)) {
      module_load_include('inc', 'update', 'update.compare');
      $data = update_calculate_project_data($available);
      // First, populate the requirements for core:
      $requirements['update_core'] = _update_requirement_check($data['drupal'], 'core');
      // We don't want to check drupal a second time.
      unset($data['drupal']);
      if (!empty($data)) {
        // Now, sort our $data array based on each project's status. The
        // status constants are numbered in the right order of precedence, so
        // we just need to make sure the projects are sorted in ascending
        // order of status, and we can look at the first project we find.
        uasort($data, '_update_project_status_sort');
        $first_project = reset($data);
        $requirements['update_contrib'] = _update_requirement_check($first_project, 'contrib');
      }
    }
    else {
      $requirements['update_core']['title'] = t('Drupal core update status');
      $requirements['update_core']['value'] = t('No update data available');
      $requirements['update_core']['severity'] = REQUIREMENT_WARNING;
      $requirements['update_core']['reason'] = UPDATE_UNKNOWN;
      $requirements['update_core']['description'] = _update_no_data();
    }
  }
  return $requirements;
}
```

---
_Drupal 7.103 · [modules/update/update.install](https://github.com/drupal/drupal/blob/7.103/modules/update/update.install) · Licensed GPL-2.0-or-later (see LICENSE)._
