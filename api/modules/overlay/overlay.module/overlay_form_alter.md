# overlay_form_alter()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 84–93 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L84-L93)
- **Module/theme:** overlay
- **Implements:** [hook_form_alter()](../../system/system.api.php/hook_form_alter.md)

## Signature

```php
function overlay_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_alter().
```

## Code

```php
function overlay_form_alter(&$form, &$form_state) {
  // Add a hidden element to prevent dropping out of the overlay when a form is
  // submitted inside the overlay using a GET method.
  if (isset($form['#method']) && $form['#method'] == 'get' && isset($_REQUEST['render']) && $_REQUEST['render'] == 'overlay' && !isset($form['render'])) {
    $form['render'] = array(
      '#type' => 'hidden',
      '#value' => 'overlay',
    );
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
