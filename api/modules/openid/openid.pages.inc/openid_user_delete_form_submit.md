# openid_user_delete_form_submit()

- **Type:** Function
- **File:** [`modules/openid/openid.pages.inc`](_file.md), lines 106–116 · [local source](../../../../source/modules/openid/openid.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc#L106-L116)
- **Module/theme:** openid

## Signature

```php
function openid_user_delete_form_submit($form, &$form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function openid_user_delete_form_submit($form, &$form_state) {
  $query = db_delete('authmap')
    ->condition('uid', $form_state['build_info']['args'][0]->uid)
    ->condition('aid', $form_state['build_info']['args'][1])
    ->condition('module', 'openid')
    ->execute();
  if ($query) {
    drupal_set_message(t('OpenID deleted.'));
  }
  $form_state['redirect'] = 'user/' . $form_state['build_info']['args'][0]->uid . '/openid';
}
```

---
_Drupal 7.103 · [modules/openid/openid.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
