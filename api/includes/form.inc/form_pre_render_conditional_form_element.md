# form_pre_render_conditional_form_element()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3283–3298 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3283-L3298)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_pre_render_conditional_form_element($element)
```

## Documentation

```text
Adds form element theming to an element if its title or description is set.

This is used as a pre render function for checkboxes and radios.
```

## Code

```php
function form_pre_render_conditional_form_element($element) {
  $t = get_t();
  // Set the element's title attribute to show #title as a tooltip, if needed.
  if (isset($element['#title']) && $element['#title_display'] == 'attribute') {
    $element['#attributes']['title'] = $element['#title'];
    if (!empty($element['#required'])) {
      // Append an indication that this field is required.
      $element['#attributes']['title'] .= ' (' . $t('Required') . ')';
    }
  }

  if (isset($element['#title']) || isset($element['#description'])) {
    $element['#theme_wrappers'][] = 'form_element';
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
