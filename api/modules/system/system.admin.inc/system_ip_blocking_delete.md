# system_ip_blocking_delete()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1480–1486 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1480-L1486)
- **Module/theme:** system

## Signature

```php
function system_ip_blocking_delete($form, &$form_state, $iid)
```

## Documentation

```text
IP deletion confirm page.

@see system_ip_blocking_delete_submit()
```

## Code

```php
function system_ip_blocking_delete($form, &$form_state, $iid) {
  $form['blocked_ip'] = array(
    '#type' => 'value',
    '#value' => $iid,
  );
  return confirm_form($form, t('Are you sure you want to delete %ip?', array('%ip' => $iid['ip'])), 'admin/config/people/ip-blocking', t('This action cannot be undone.'), t('Delete'), t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
