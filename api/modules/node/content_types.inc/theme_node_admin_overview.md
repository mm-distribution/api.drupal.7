# theme_node_admin_overview()

- **Type:** Function
- **File:** [`modules/node/content_types.inc`](_file.md), lines 67–75 · [local source](../../../../source/modules/node/content_types.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc#L67-L75)
- **Module/theme:** node
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_node_admin_overview($variables)
```

## Documentation

```text
Returns HTML for a node type description for the content type admin overview page.

@param $variables
  An associative array containing:
  - name: The human-readable name of the content type.
  - type: An object containing the 'type' (machine name) and 'description' of
    the content type.

@ingroup themeable
```

## Code

```php
function theme_node_admin_overview($variables) {
  $name = $variables['name'];
  $type = $variables['type'];

  $output = check_plain($name);
  $output .= ' <small>' . t('(Machine name: @type)', array('@type' => $type->type)) . '</small>';
  $output .= '<div class="description">' . filter_xss_admin($type->description) . '</div>';
  return $output;
}
```

---
_Drupal 7.103 · [modules/node/content_types.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
