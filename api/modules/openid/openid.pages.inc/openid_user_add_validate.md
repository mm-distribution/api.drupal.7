# openid_user_add_validate()

- **Type:** Function
- **File:** [`modules/openid/openid.pages.inc`](_file.md), lines 81–87 · [local source](../../../../source/modules/openid/openid.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc#L81-L87)
- **Module/theme:** openid

## Signature

```php
function openid_user_add_validate($form, &$form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function openid_user_add_validate($form, &$form_state) {
  // Check for existing entries.
  $claimed_id = openid_normalize($form_state['values']['openid_identifier']);
  if (db_query("SELECT authname FROM {authmap} WHERE authname = :authname", (array(':authname' => $claimed_id)))->fetchField()) {
    form_set_error('openid_identifier', t('That OpenID is already in use on this site.'));
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
