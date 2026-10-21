# openid_redirect_form()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 110–129 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L110-L129)
- **Module/theme:** openid

## Signature

```php
function openid_redirect_form($form, &$form_state, $url, $message)
```

## Documentation

_No docblock in source._

## Code

```php
function openid_redirect_form($form, &$form_state, $url, $message) {
  $form['#action'] = $url;
  $form['#method'] = "post";
  foreach ($message as $key => $value) {
    $form[$key] = array(
      '#type' => 'hidden',
      '#name' => $key,
      '#value' => $value,
    );
  }
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#prefix' => '<noscript><div>',
    '#suffix' => '</div></noscript>',
    '#value' => t('Send'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
