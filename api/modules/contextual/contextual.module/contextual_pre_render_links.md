# contextual_pre_render_links()

- **Type:** Function
- **File:** [`modules/contextual/contextual.module`](_file.md), lines 137–168 · [local source](../../../../source/modules/contextual/contextual.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module#L137-L168)
- **Module/theme:** contextual

## Signature

```php
function contextual_pre_render_links($element)
```

## Documentation

```text
Build a renderable array for contextual links.

@param $element
  A renderable array containing a #contextual_links property, which is a
  keyed array. Each key is the name of the implementing module, and each
  value is an array that forms the function arguments for
  menu_contextual_links(). For example:
  @code
    array('#contextual_links' => array(
      'block' => array('admin/structure/block/manage', array('system', 'navigation')),
      'menu' => array('admin/structure/menu/manage', array('navigation')),
    ))
  @endcode

@return
  A renderable array representing contextual links.

@see menu_contextual_links()
@see contextual_element_info()
```

## Code

```php
function contextual_pre_render_links($element) {
  // Retrieve contextual menu links.
  $items = array();
  foreach ($element['#contextual_links'] as $module => $args) {
    $items += menu_contextual_links($module, $args[0], $args[1]);
  }

  // Transform contextual links into parameters suitable for theme_link().
  $links = array();
  foreach ($items as $class => $item) {
    $class = drupal_html_class($class);
    $links[$class] = array(
      'title' => $item['title'],
      'href' => $item['href'],
    );
    // @todo theme_links() should *really* use the same parameters as l().
    $item['localized_options'] += array('query' => array());
    $item['localized_options']['query'] += drupal_get_destination();
    $links[$class] += $item['localized_options'];
  }
  $element['#links'] = $links;

  // Allow modules to alter the renderable contextual links element.
  drupal_alter('contextual_links_view', $element, $items);

  // If there are no links, tell drupal_render() to abort rendering.
  if (empty($element['#links'])) {
    $element['#printed'] = TRUE;
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/contextual/contextual.module](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module) · Licensed GPL-2.0-or-later (see LICENSE)._
