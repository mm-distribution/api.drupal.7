# theme_status_report()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2607–2649 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2607-L2649)
- **Module/theme:** system
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_status_report($variables)
```

## Documentation

```text
Returns HTML for the status report.

This theme function is dependent on install.inc being loaded, because
that's where the constants are defined.

@param $variables
  An associative array containing:
  - requirements: An array of requirements/status items. Each requirement
    is an associative array containing the following elements:
    - title: The name of the requirement.
    - value: (optional) The current value (version, time, level, etc).
    - description: (optional) The description of the requirement.
    - severity: (optional) The requirement's result/severity level, one of:
      - REQUIREMENT_INFO: Status information.
      - REQUIREMENT_OK: The requirement is satisfied.
      - REQUIREMENT_WARNING: The requirement failed with a warning.
      - REQUIREMENT_ERROR: The requirement failed with an error.

@ingroup themeable
```

## Code

```php
function theme_status_report($variables) {
  $requirements = $variables['requirements'];
  $severities = array(
    REQUIREMENT_INFO => array(
      'title' => t('Info'),
      'class' => 'info',
    ),
    REQUIREMENT_OK => array(
      'title' => t('OK'),
      'class' => 'ok',
    ),
    REQUIREMENT_WARNING => array(
      'title' => t('Warning'),
      'class' => 'warning',
    ),
    REQUIREMENT_ERROR => array(
      'title' => t('Error'),
      'class' => 'error',
    ),
  );
  $output = '<table class="system-status-report">';

  foreach ($requirements as $requirement) {
    if (empty($requirement['#type'])) {
      $severity = $severities[isset($requirement['severity']) ? (int) $requirement['severity'] : REQUIREMENT_OK];
      $severity['icon'] = '<div title="' . $severity['title'] . '"><span class="element-invisible">' . $severity['title'] . '</span></div>';
      // The requirement's 'value' key is optional, provide a default value.
      $requirement['value'] = isset($requirement['value']) ? $requirement['value'] : '';

      // Output table row(s)
      if (!empty($requirement['description'])) {
        $output .= '<tr class="' . $severity['class'] . ' merge-down"><td class="status-icon">' . $severity['icon'] . '</td><td class="status-title">' . $requirement['title'] . '</td><td class="status-value">' . $requirement['value'] . '</td></tr>';
        $output .= '<tr class="' . $severity['class'] . ' merge-up"><td colspan="3" class="status-description">' . $requirement['description'] . '</td></tr>';
      }
      else {
        $output .= '<tr class="' . $severity['class'] . '"><td class="status-icon">' . $severity['icon'] . '</td><td class="status-title">' . $requirement['title'] . '</td><td class="status-value">' . $requirement['value'] . '</td></tr>';
      }
    }
  }

  $output .= '</table>';
  return $output;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
