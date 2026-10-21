# contextual_preprocess()

- **Type:** Function
- **File:** [`modules/contextual/contextual.module`](_file.md), lines 84–114 · [local source](../../../../source/modules/contextual/contextual.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module#L84-L114)
- **Module/theme:** contextual
- **Implements:** [hook_preprocess()](../../system/theme.api.php/hook_preprocess.md)

## Signature

```php
function contextual_preprocess(&$variables, $hook)
```

## Documentation

```text
Implements hook_preprocess().

@see contextual_pre_render_links()
```

## Code

```php
function contextual_preprocess(&$variables, $hook) {
  // Nothing to do here if the user is not permitted to access contextual links.
  if (!user_access('access contextual links')) {
    return;
  }

  $hooks = theme_get_registry(FALSE);

  // Determine the primary theme function argument.
  if (!empty($hooks[$hook]['variables'])) {
    $keys = array_keys($hooks[$hook]['variables']);
    $key = $keys[0];
  }
  elseif (!empty($hooks[$hook]['render element'])) {
    $key = $hooks[$hook]['render element'];
  }
  if (!empty($key) && isset($variables[$key])) {
    $element = $variables[$key];
  }

  if (isset($element) && is_array($element) && !empty($element['#contextual_links'])) {
    // Initialize the template variable as a renderable array.
    $variables['title_suffix']['contextual_links'] = array(
      '#type' => 'contextual_links',
      '#contextual_links' => $element['#contextual_links'],
      '#element' => $element,
    );
    // Mark this element as potentially having contextual links attached to it.
    $variables['classes_array'][] = 'contextual-links-region';
  }
}
```

---
_Drupal 7.103 · [modules/contextual/contextual.module](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module) · Licensed GPL-2.0-or-later (see LICENSE)._
