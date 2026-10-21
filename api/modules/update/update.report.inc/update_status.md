# update_status()

- **Type:** Function
- **File:** [`modules/update/update.report.inc`](_file.md), lines 13–22 · [local source](../../../../source/modules/update/update.report.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.report.inc#L13-L22)
- **Module/theme:** update

## Signature

```php
function update_status()
```

## Documentation

```text
Page callback: Generates a page about the update status of projects.

@see update_menu()
```

## Code

```php
function update_status() {
  if ($available = update_get_available(TRUE)) {
    module_load_include('inc', 'update', 'update.compare');
    $data = update_calculate_project_data($available);
    return theme('update_report', array('data' => $data));
  }
  else {
    return theme('update_report', array('data' => _update_no_data()));
  }
}
```

---
_Drupal 7.103 · [modules/update/update.report.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.report.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
