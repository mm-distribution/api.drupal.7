# color_scheme_form_validate()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 349–356 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L349-L356)
- **Module/theme:** color

## Signature

```php
function color_scheme_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for color_scheme_form().

@see color_scheme_form_submit()
```

## Code

```php
function color_scheme_form_validate($form, &$form_state) {
  // Only accept hexadecimal CSS color strings to avoid XSS upon use.
  foreach ($form_state['values']['palette'] as $key => $color) {
    if (!color_valid_hexadecimal_string($color)) {
      form_set_error('palette][' . $key, t('%name must be a valid hexadecimal CSS color value.', array('%name' => $form['color']['palette'][$key]['#title'])));
    }
  }
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
