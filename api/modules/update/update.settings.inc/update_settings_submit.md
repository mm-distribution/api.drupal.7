# update_settings_submit()

- **Type:** Function
- **File:** [`modules/update/update.settings.inc`](_file.md), lines 109–129 · [local source](../../../../source/modules/update/update.settings.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.settings.inc#L109-L129)
- **Module/theme:** update

## Signature

```php
function update_settings_submit($form, $form_state)
```

## Documentation

```text
Form submission handler for update_settings().

Also invalidates the cache of available updates if the "Check for updates of
disabled and uninstalled modules and themes" setting is being changed. The
available updates report needs to refetch available update data after this
setting changes or it would show misleading things (e.g., listing the
disabled projects on the site with the "No available releases found"
warning).

@see update_settings_validate()
```

## Code

```php
function update_settings_submit($form, $form_state) {
  $op = $form_state['values']['op'];

  if (empty($form_state['notify_emails'])) {
    variable_del('update_notify_emails');
  }
  else {
    variable_set('update_notify_emails', $form_state['notify_emails']);
  }
  unset($form_state['notify_emails']);
  unset($form_state['values']['update_notify_emails']);

  // See if the update_check_disabled setting is being changed, and if so,
  // invalidate all cached update status data.
  $check_disabled = variable_get('update_check_disabled', FALSE);
  if ($form_state['values']['update_check_disabled'] != $check_disabled) {
    _update_cache_clear();
  }

  system_settings_form_submit($form, $form_state);
}
```

---
_Drupal 7.103 · [modules/update/update.settings.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.settings.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
