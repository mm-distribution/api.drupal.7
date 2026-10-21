# dblog_clear_log_form()

- **Type:** Function
- **File:** [`modules/dblog/dblog.admin.inc`](_file.md), lines 407–422 · [local source](../../../../source/modules/dblog/dblog.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc#L407-L422)
- **Module/theme:** dblog
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function dblog_clear_log_form($form)
```

## Documentation

```text
Form constructor for the form that clears out the log.

@see dblog_clear_log_submit()
@ingroup forms
```

## Code

```php
function dblog_clear_log_form($form) {
  $form['dblog_clear'] = array(
    '#type' => 'fieldset',
    '#title' => t('Clear log messages'),
    '#description' => t('This will permanently remove the log messages from the database.'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
  );
  $form['dblog_clear']['clear'] = array(
    '#type' => 'submit',
    '#value' => t('Clear log messages'),
    '#submit' => array('dblog_clear_log_submit'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
