# theme_toolbar_toggle()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 96–105 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L96-L105)
- **Module/theme:** toolbar
- **Topics:** themable

## Signature

```php
function theme_toolbar_toggle($variables)
```

## Documentation

```text
Formats an element used to toggle the toolbar drawer's visibility.

@param $variables
  An associative array containing:
  - collapsed: A boolean value representing the toolbar drawer's visibility.
  - attributes: An associative array of HTML attributes.

@return
  An HTML string representing the element for toggling.

@ingroup themable
```

## Code

```php
function theme_toolbar_toggle($variables) {
  if ($variables['collapsed']) {
    $toggle_text = t('Show shortcuts');
  }
  else {
    $toggle_text = t('Hide shortcuts');
    $variables['attributes']['class'][] = 'toggle-active';
  }
  return l($toggle_text, 'toolbar/toggle', array('query' => drupal_get_destination(), 'attributes' => array('title' => $toggle_text) + $variables['attributes']));
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
