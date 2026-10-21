# bartik_field__taxonomy_term_reference()

- **Type:** Function
- **File:** [`themes/bartik/template.php`](_file.md), lines 137–156 · [local source](../../../../source/themes/bartik/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php#L137-L156)
- **Module/theme:** bartik

## Signature

```php
function bartik_field__taxonomy_term_reference($variables)
```

## Documentation

```text
Implements theme_field__field_type().
```

## Code

```php
function bartik_field__taxonomy_term_reference($variables) {
  $output = '';

  // Render the label, if it's not hidden.
  if (!$variables['label_hidden']) {
    $output .= '<h3 class="field-label">' . $variables['label'] . ': </h3>';
  }

  // Render the items.
  $output .= ($variables['element']['#label_display'] == 'inline') ? '<ul class="links inline">' : '<ul class="links">';
  foreach ($variables['items'] as $delta => $item) {
    $output .= '<li class="taxonomy-term-reference-' . $delta . '"' . $variables['item_attributes'][$delta] . '>' . drupal_render($item) . '</li>';
  }
  $output .= '</ul>';

  // Render the top-level DIV.
  $output = '<div class="' . $variables['classes'] . (!in_array('clearfix', $variables['classes_array']) ? ' clearfix' : '') . '"' . $variables['attributes'] .'>' . $output . '</div>';

  return $output;
}
```

---
_Drupal 7.103 · [themes/bartik/template.php](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
