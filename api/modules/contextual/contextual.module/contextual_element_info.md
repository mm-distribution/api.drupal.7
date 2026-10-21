# contextual_element_info()

- **Type:** Function
- **File:** [`modules/contextual/contextual.module`](_file.md), lines 60–77 · [local source](../../../../source/modules/contextual/contextual.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module#L60-L77)
- **Module/theme:** contextual
- **Implements:** [hook_element_info()](../../system/system.api.php/hook_element_info.md)

## Signature

```php
function contextual_element_info()
```

## Documentation

```text
Implements hook_element_info().
```

## Code

```php
function contextual_element_info() {
  $types['contextual_links'] = array(
    '#pre_render' => array('contextual_pre_render_links'),
    '#theme' => 'links__contextual',
    '#links' => array(),
    '#prefix' => '<div class="contextual-links-wrapper">',
    '#suffix' => '</div>',
    '#attributes' => array(
      'class' => array('contextual-links'),
    ),
    '#attached' => array(
      'library' => array(
        array('contextual', 'contextual-links'),
      ),
    ),
  );
  return $types;
}
```

---
_Drupal 7.103 · [modules/contextual/contextual.module](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module) · Licensed GPL-2.0-or-later (see LICENSE)._
