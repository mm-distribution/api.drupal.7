# update_check_requirements()

- **Type:** Function
- **File:** [`update.php`](_file.md), lines 353–369 · [local source](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php#L353-L369)

## Signature

```php
function update_check_requirements($skip_warnings = FALSE)
```

## Documentation

```text
Checks update requirements and reports errors and (optionally) warnings.

@param $skip_warnings
  (optional) If set to TRUE, requirement warnings will be ignored, and a
  report will only be issued if there are requirement errors. Defaults to
  FALSE.
```

## Code

```php
function update_check_requirements($skip_warnings = FALSE) {
  // Check requirements of all loaded modules.
  $requirements = module_invoke_all('requirements', 'update');
  $requirements += update_extra_requirements();
  $severity = drupal_requirements_severity($requirements);

  // If there are errors, always display them. If there are only warnings, skip
  // them if the caller has indicated they should be skipped.
  if ($severity == REQUIREMENT_ERROR || ($severity == REQUIREMENT_WARNING && !$skip_warnings)) {
    update_task_list('requirements');
    drupal_set_title('Requirements problem');
    $status_report = theme('status_report', array('requirements' => $requirements));
    $status_report .= 'Check the error messages and <a href="' . check_url(drupal_requirements_url($severity)) . '">try again</a>.';
    print theme('update_page', array('content' => $status_report));
    exit();
  }
}
```

---
_Drupal 7.103 · [update.php](https://github.com/drupal/drupal/blob/7.103/update.php) · Licensed GPL-2.0-or-later (see LICENSE)._
