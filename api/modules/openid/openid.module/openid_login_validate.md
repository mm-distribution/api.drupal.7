# openid_login_validate()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 242–249 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L242-L249)
- **Module/theme:** openid

## Signature

```php
function openid_login_validate($form, &$form_state)
```

## Documentation

```text
Login form _validate hook
```

## Code

```php
function openid_login_validate($form, &$form_state) {
  $return_to = $form_state['values']['openid.return_to'];
  if (empty($return_to)) {
    $return_to = url('', array('absolute' => TRUE));
  }

  openid_begin($form_state['values']['openid_identifier'], $return_to, $form_state['values']);
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
