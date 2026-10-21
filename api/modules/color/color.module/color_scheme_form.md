# color_scheme_form()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 171–253 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L171-L253)
- **Module/theme:** color
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function color_scheme_form($complete_form, &$form_state, $theme)
```

## Documentation

```text
Form constructor for the color configuration form for a particular theme.

@param $theme
  The machine name of the theme whose color settings are being configured.

@see color_scheme_form_validate()
@see color_scheme_form_submit()
@ingroup forms
```

## Code

```php
function color_scheme_form($complete_form, &$form_state, $theme) {
  $base = drupal_get_path('module', 'color');
  $info = color_get_info($theme);

  $info['schemes'][''] = array('title' => t('Custom'), 'colors' => array());
  $color_sets = array();
  $schemes = array();
  foreach ($info['schemes'] as $key => $scheme) {
    $color_sets[$key] = $scheme['title'];
    $schemes[$key] = $scheme['colors'];
    $schemes[$key] += $info['schemes']['default']['colors'];
  }

  // See if we're using a predefined scheme.
  // Note: we use the original theme when the default scheme is chosen.
  $current_scheme = variable_get('color_' . $theme . '_palette', array());
  foreach ($schemes as $key => $scheme) {
    if ($current_scheme == $scheme) {
      $scheme_name = $key;
      break;
    }
  }
  if (empty($scheme_name)) {
    if (empty($current_scheme)) {
      $scheme_name = 'default';
    }
    else {
      $scheme_name = '';
    }
  }

  // Add scheme selector.
  $form['scheme'] = array(
    '#type' => 'select',
    '#title' => t('Color set'),
    '#options' => $color_sets,
    '#default_value' => $scheme_name,
    '#attached' => array(
      // Add Farbtastic color picker.
      'library' => array(
        array('system', 'farbtastic'),
      ),
      // Add custom CSS.
      'css' => array(
        $base . '/color.css' => array(),
      ),
      // Add custom JavaScript.
      'js' => array(
        $base . '/color.js',
        array(
          'data' => array(
            'color' => array(
              'reference' => color_get_palette($theme, TRUE),
              'schemes' => $schemes,
            ),
            'gradients' => $info['gradients'],
          ),
          'type' => 'setting',
        ),
      ),
    ),
  );

  // Add palette fields.
  $palette = color_get_palette($theme);
  $names = $info['fields'];
  $form['palette']['#tree'] = TRUE;
  foreach ($palette as $name => $value) {
    if (isset($names[$name])) {
      $form['palette'][$name] = array(
        '#type' => 'textfield',
        '#title' => check_plain($names[$name]),
        '#value_callback' => 'color_palette_color_value',
        '#default_value' => $value,
        '#size' => 8,
      );
    }
  }
  $form['theme'] = array('#type' => 'value', '#value' => $theme);
  $form['info'] = array('#type' => 'value', '#value' => $info);

  return $form;
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
