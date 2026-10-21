# openid_authentication_page()

- **Type:** Function
- **File:** [`modules/openid/openid.pages.inc`](_file.md), lines 11–24 · [local source](../../../../source/modules/openid/openid.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc#L11-L24)
- **Module/theme:** openid

## Signature

```php
function openid_authentication_page()
```

## Documentation

```text
Menu callback; Process an OpenID authentication.
```

## Code

```php
function openid_authentication_page() {
  $result = openid_complete();
  switch ($result['status']) {
    case 'success':
      return openid_authentication($result);
    case 'failed':
      drupal_set_message(t('OpenID login failed.'), 'error');
      break;
    case 'cancel':
      drupal_set_message(t('OpenID login cancelled.'));
      break;
  }
  drupal_goto();
}
```

---
_Drupal 7.103 · [modules/openid/openid.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
