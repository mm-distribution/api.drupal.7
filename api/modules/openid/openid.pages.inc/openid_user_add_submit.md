# openid_user_add_submit()

- **Type:** Function
- **File:** [`modules/openid/openid.pages.inc`](_file.md), lines 89–92 · [local source](../../../../source/modules/openid/openid.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc#L89-L92)
- **Module/theme:** openid

## Signature

```php
function openid_user_add_submit($form, &$form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function openid_user_add_submit($form, &$form_state) {
  $return_to = url('user/' . arg(1) . '/openid', array('absolute' => TRUE));
  openid_begin($form_state['values']['openid_identifier'], $return_to);
}
```

---
_Drupal 7.103 · [modules/openid/openid.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
