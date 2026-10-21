# theme_update_status_label()

- **Type:** Function
- **File:** [`modules/update/update.report.inc`](_file.md), lines 264–282 · [local source](../../../../source/modules/update/update.report.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.report.inc#L264-L282)
- **Module/theme:** update
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_update_status_label($variables)
```

## Documentation

```text
Returns HTML for a label to display for a project's update status.

@param array $variables
  An associative array containing:
  - status: The integer code for a project's current update status.

@see update_calculate_project_data()
@ingroup themeable
```

## Code

```php
function theme_update_status_label($variables) {
  switch ($variables['status']) {
    case UPDATE_NOT_SECURE:
      return '<span class="security-error">' . t('Security update required!') . '</span>';

    case UPDATE_REVOKED:
      return '<span class="revoked">' . t('Revoked!') . '</span>';

    case UPDATE_NOT_SUPPORTED:
      return '<span class="not-supported">' . t('Not supported!') . '</span>';

    case UPDATE_NOT_CURRENT:
      return '<span class="not-current">' . t('Update available') . '</span>';

    case UPDATE_CURRENT:
      return '<span class="current">' . t('Up to date') . '</span>';

  }
}
```

---
_Drupal 7.103 · [modules/update/update.report.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.report.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
