# dblog_filter_form_validate()

- **Type:** Function
- **File:** [`modules/dblog/dblog.admin.inc`](_file.md), lines 372–376 · [local source](../../../../source/modules/dblog/dblog.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc#L372-L376)
- **Module/theme:** dblog

## Signature

```php
function dblog_filter_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for dblog_filter_form().

@see dblog_filter_form_submit()
```

## Code

```php
function dblog_filter_form_validate($form, &$form_state) {
  if ($form_state['values']['op'] == t('Filter') && empty($form_state['values']['type']) && empty($form_state['values']['severity'])) {
    form_set_error('type', t('You must select something to filter by.'));
  }
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
