# _openid_user_login_form_alter()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 136–175 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L136-L175)
- **Module/theme:** openid

## Signature

```php
function _openid_user_login_form_alter(&$form, &$form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function _openid_user_login_form_alter(&$form, &$form_state) {
  $form['#attached']['css'][] = drupal_get_path('module', 'openid') . '/openid.css';
  $form['#attached']['js'][] = drupal_get_path('module', 'openid') . '/openid.js';
  $form['#attached']['library'][] = array('system', 'jquery.cookie');
  if (!empty($form_state['input']['openid_identifier'])) {
    $form['name']['#required'] = FALSE;
    $form['pass']['#required'] = FALSE;
    unset($form['#submit']);
    $form['#validate'] = array('openid_login_validate');
  }

  $items = array();
  $items[] = array(
    'data' => l(t('Log in using OpenID'), '#openid-login', array('external' => TRUE)),
    'class' => array('openid-link'),
  );
  $items[] = array(
    'data' => l(t('Cancel OpenID login'), '#', array('external' => TRUE)),
    'class' => array('user-link'),
  );

  $form['openid_links'] = array(
    '#theme' => 'item_list',
    '#items' => $items,
    '#attributes' => array('class' => array('openid-links')),
    '#weight' => 1,
  );

  $form['links']['#weight'] = 2;

  $form['openid_identifier'] = array(
    '#type' => 'textfield',
    '#title' => t('Log in using OpenID'),
    '#size' => $form['name']['#size'],
    '#maxlength' => 255,
    '#weight' => -1,
    '#description' => l(t('What is OpenID?'), 'http://openid.net/', array('external' => TRUE)),
  );
  $form['openid.return_to'] = array('#type' => 'hidden', '#value' => url('openid/authenticate', array('absolute' => TRUE, 'query' => user_login_destination())));
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
