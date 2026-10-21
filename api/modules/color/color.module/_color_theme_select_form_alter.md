# _color_theme_select_form_alter()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 64–74 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L64-L74)
- **Module/theme:** color

## Signature

```php
function _color_theme_select_form_alter(&$form, &$form_state)
```

## Documentation

```text
Helper for hook_form_FORM_ID_alter() implementations.
```

## Code

```php
function _color_theme_select_form_alter(&$form, &$form_state) {
  // Use the generated screenshot in the theme list.
  $themes = list_themes();
  foreach (element_children($form) as $theme) {
    if ($screenshot = variable_get('color_' . $theme . '_screenshot')) {
      if (isset($form[$theme]['screenshot'])) {
        $form[$theme]['screenshot']['#markup'] = theme('image', array('path' => $screenshot, 'title' => '', 'attributes' => array('class' => array('screenshot'))));
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
