# drupal_pre_render_links()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6008–6022 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6008-L6022)

## Signature

```php
function drupal_pre_render_links($element)
```

## Documentation

```text
#pre_render callback that collects child links into a single array.

This function can be added as a pre_render callback for a renderable array,
usually one which will be themed by theme_links(). It iterates through all
unrendered children of the element, collects any #links properties it finds,
merges them into the parent element's #links array, and prevents those
children from being rendered separately.

The purpose of this is to allow links to be logically grouped into related
categories, so that each child group can be rendered as its own list of
links if drupal_render() is called on it, but calling drupal_render() on the
parent element will still produce a single list containing all the remaining
links, regardless of what group they were in.

A typical example comes from node links, which are stored in a renderable
array similar to this:
@code
$node->content['links'] = array(
  '#theme' => 'links__node',
  '#pre_render' => array('drupal_pre_render_links'),
  'comment' => array(
    '#theme' => 'links__node__comment',
    '#links' => array(
      // An array of links associated with node comments, suitable for
      // passing in to theme_links().
    ),
  ),
  'statistics' => array(
    '#theme' => 'links__node__statistics',
    '#links' => array(
      // An array of links associated with node statistics, suitable for
      // passing in to theme_links().
    ),
  ),
  'translation' => array(
    '#theme' => 'links__node__translation',
    '#links' => array(
      // An array of links associated with node translation, suitable for
      // passing in to theme_links().
    ),
  ),
);
@endcode

In this example, the links are grouped by functionality, which can be
helpful to themers who want to display certain kinds of links independently.
For example, adding this code to node.tpl.php will result in the comment
links being rendered as a single list:
@code
print render($content['links']['comment']);
@endcode

(where $node->content has been transformed into $content before handing
control to the node.tpl.php template).

The pre_render function defined here allows the above flexibility, but also
allows the following code to be used to render all remaining links into a
single list, regardless of their group:
@code
print render($content['links']);
@endcode

In the above example, this will result in the statistics and translation
links being rendered together in a single list (but not the comment links,
which were rendered previously on their own).

Because of the way this function works, the individual properties of each
group (for example, a group-specific #theme property such as
'links__node__comment' in the example above, or any other property such as
#attributes or #pre_render that is attached to it) are only used when that
group is rendered on its own. When the group is rendered together with other
children, these child-specific properties are ignored, and only the overall
properties of the parent are used.
```

## Code

```php
function drupal_pre_render_links($element) {
  $element += array('#links' => array());
  foreach (element_children($element) as $key) {
    $child = &$element[$key];
    // If the child has links which have not been printed yet and the user has
    // access to it, merge its links in to the parent.
    if (isset($child['#links']) && empty($child['#printed']) && (!isset($child['#access']) || $child['#access'])) {
      $element['#links'] += $child['#links'];
      // Mark the child as having been printed already (so that its links
      // cannot be mistakenly rendered twice).
      $child['#printed'] = TRUE;
    }
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
