# overlay_form_user_profile_form_alter()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 98–117 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L98-L117)
- **Module/theme:** overlay
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function overlay_form_user_profile_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function overlay_form_user_profile_form_alter(&$form, &$form_state) {
  if ($form['#user_category'] == 'account') {
    $account = $form['#user'];
    if (user_access('access overlay', $account)) {
      $form['overlay_control'] = array(
        '#type' => 'fieldset',
        '#title' => t('Administrative overlay'),
        '#weight' => 4,
        '#collapsible' => TRUE,
      );

      $form['overlay_control']['overlay'] = array(
        '#type' => 'checkbox',
        '#title' => t('Use the overlay for administrative pages.'),
        '#description' => t('Show administrative pages on top of the page you started from.'),
        '#default_value' => isset($account->data['overlay']) ? $account->data['overlay'] : 1,
      );
    }
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
