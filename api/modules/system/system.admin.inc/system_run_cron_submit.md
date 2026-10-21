# system_run_cron_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1663–1673 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1663-L1673)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_run_cron_submit($form, &$form_state)
```

## Documentation

```text
Submit callback; run cron.

@ingroup forms
```

## Code

```php
function system_run_cron_submit($form, &$form_state) {
  // Run cron manually from Cron form.
  if (drupal_cron_run()) {
    drupal_set_message(t('Cron run successfully.'));
  }
  else {
    drupal_set_message(t('Cron run failed.'), 'error');
  }

  drupal_goto('admin/config/system/cron');
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
