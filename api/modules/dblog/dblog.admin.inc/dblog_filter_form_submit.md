# dblog_filter_form_submit()

- **Type:** Function
- **File:** [`modules/dblog/dblog.admin.inc`](_file.md), lines 383–399 · [local source](../../../../source/modules/dblog/dblog.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc#L383-L399)
- **Module/theme:** dblog

## Signature

```php
function dblog_filter_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for dblog_filter_form().

@see dblog_filter_form_validate()
```

## Code

```php
function dblog_filter_form_submit($form, &$form_state) {
  $op = $form_state['values']['op'];
  $filters = dblog_filters();
  switch ($op) {
    case t('Filter'):
      foreach ($filters as $name => $filter) {
        if (isset($form_state['values'][$name])) {
          $_SESSION['dblog_overview_filter'][$name] = $form_state['values'][$name];
        }
      }
      break;
    case t('Reset'):
      $_SESSION['dblog_overview_filter'] = array();
      break;
  }
  return 'admin/reports/dblog';
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
