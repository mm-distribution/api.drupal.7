# openid_user_add()

- **Type:** Function
- **File:** [`modules/openid/openid.pages.inc`](_file.md), lines 71–79 · [local source](../../../../source/modules/openid/openid.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc#L71-L79)
- **Module/theme:** openid
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function openid_user_add()
```

## Documentation

```text
Form builder; Add an OpenID identity.

@ingroup forms
@see openid_user_add_validate()
```

## Code

```php
function openid_user_add() {
  $form['openid_identifier'] = array(
    '#type' => 'textfield',
    '#title' => t('OpenID'),
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Add an OpenID'));
  return $form;
}
```

---
_Drupal 7.103 · [modules/openid/openid.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
